
from launch import LaunchDescription

from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    node_1=Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    node_2=Node(
        package="turtlesim",
        executable="turtlesim_node",
        namespace="tf"
    )

    rotate =ExecuteProcess(
        cmd=["ros2 action send_goal /tf/turtle1/rotate_absolute turtlesim/action/RotateAbsolute \"{'theta': 3.14}\""],
        output="both",
        shell=True
        )
    

    return LaunchDescription([node_1,node_2,rotate])
