import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from imageai.Detection import ObjectDetection
import os, shutil
import signal

# We define a class named ImageSubscriber to subscribe 
# to the topic where the images of the camera are published  

execution_path = os.getcwd()
index = 0
is_launch = True

def SignalHandler_SIGINT(SignalNumber,Frame):
  print('Exit pressed !')
  print('Saving the video of the session ...')
  
  #Break the infinit loop
  global is_launch
  is_launch = False

  #Get the total number of frames
  nb_frame = 0
  for path in os.listdir("Frames/"):
    if os.path.isfile(os.path.join("Frames/", path)):
      nb_frame += 1

  #Make a video with all the images from FramesAnalysed folder
  img_array = []
  for i in range(nb_frame):
    if os.path.isfile('FramesAnalysed/frameAnalysed%d.png' % i):
      img_array.append(cv2.imread('FramesAnalysed/frameAnalysed%d.png' % i))
    elif os.path.isfile('Frames/Frame%d.png' % i):
      img_array.append(cv2.imread('Frames/Frame%d.png' % i))

  height,width,layers = img_array[1].shape

  #Get number of video already saved
  nb_vid = 0
  for path in os.listdir("Dump_IA_detection_vid/"):
    if os.path.isfile(os.path.join("Dump_IA_detection_vid/", path)):
      nb_vid += 1

  print('Assembling the video ...')
  out = cv2.VideoWriter('Dump_IA_detection_vid/IA-detections_vid%d.avi' % nb_vid,cv2.VideoWriter_fourcc(*'DIVX'), 15,(width,height))
  for j in range(len(img_array)):
    out.write(img_array[j])
    print(j)
  out.release()

  #Delete all images in Frames/
  frame_folder_path = 'Frames/'
  for filename in os.listdir(frame_folder_path):
    file_path = os.path.join(frame_folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

  #Delete all images in FramesAnalysed/
  frame_folder_path = 'FramesAnalysed/'
  for filename in os.listdir(frame_folder_path):
    file_path = os.path.join(frame_folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
  print("Done !")


class ImageSubscriber(Node):

  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(Image, '/camera/image_raw', self.listener_callback, 10)       
    self.br = CvBridge()
   

  def listener_callback(self, data):
    global index
    index = 0
    for path in os.listdir("Frames/"):
      if os.path.isfile(os.path.join("Frames/", path)):
        index += 1
    self.get_logger().info('Receiving video frame%d' % index)
    current_frame = self.br.imgmsg_to_cv2(data)
    cv2.imwrite("Frames/Frame%d.png" % index, current_frame)

def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  signal.signal(signal.SIGINT,SignalHandler_SIGINT)
  while(is_launch):
    rclpy.spin_once(image_subscriber)

    detector = ObjectDetection()  
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolov3.pt"))
    detector.loadModel()

    if os.path.isfile("Frames/Frame%d.png" % index):
      detections = detector.detectObjectsFromImage(input_image="Frames/Frame%d.png" % index,
                                                   output_image_path=os.path.join(execution_path, "FramesAnalysed/frameAnalysed%d.png" % index),
                                                   minimum_percentage_probability=30)
    for eachObject in detections:
      print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
      print("--------------------------------")


    if os.path.isfile("FramesAnalysed/frameAnalysed%d.png" % index):
      img_analysed = cv2.imread("FramesAnalysed/frameAnalysed%d.png" % index)
      cv2.imshow("IA_Detection", img_analysed)
      cv2.waitKey(1)
    elif os.path.isfile("Frames/Frame%d.png" % index):
      img = cv2.imread("Frames/Frame%d.png" % index)
      cv2.imshow("IA_Detection", img)
      cv2.waitKey(1)

  cv2.destroyAllWindows()
  image_subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()