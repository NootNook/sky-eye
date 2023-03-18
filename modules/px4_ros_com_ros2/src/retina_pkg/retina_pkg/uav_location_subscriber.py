import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from px4_msgs.msg import SensorGps

topic_gps_position = '/fmu/out/vehicle_gps_position'
class UAVLocationSubscriber(Node):

  def __init__(self):
    super().__init__('gps_location_subscriber')
      
    self.subscription = self.create_subscription(
      SensorGps, 
      topic_gps_position, 
      self.listener_callback, 
      qos_profile_sensor_data
    )
    
    self.subscription
   
  def listener_callback(self, msg):
    self.get_logger().info('Receiving gps location of uav : "%s %s"' % (msg.lat, msg.lon))

    
  
def main(args=None):
  rclpy.init(args=args)
  
  uav_location_subscriber = UAVLocationSubscriber()

  print("start")

  rclpy.spin(uav_location_subscriber)

  uav_location_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()