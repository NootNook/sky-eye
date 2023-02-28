using UnityEngine;

namespace ROS2
{

public class SubPointCloud : MonoBehaviour
{
    private ROS2UnityComponent ros2Unity;
    private ROS2Node ros2Node;
    private ISubscription<sensor_msgs.msg.PointCloud2> chatter_sub;

    void Start()
    {
        ros2Unity = GetComponent<ROS2UnityComponent>();
    }

    void Update()
    {
        if (ros2Node == null && ros2Unity.Ok())
        {
            ros2Node = ros2Unity.CreateNode("SubPointCloud");
            chatter_sub = ros2Node.CreateSubscription<sensor_msgs.msg.PointCloud2>("/ray/pointcloud2", 
                msg => Debug.Log("On a le nuage de point mon reuf enfin :)"));
        }
    }
}

}  // namespace ROS2
