import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command

def generate_launch_description():

    p_value=ParameterValue(Command("xacro /home/zjt/d2lros2/laser/src/install/laser_nav2/share/laser_nav2/urdf/car.urdf"))
    robot_state_publisher_=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":p_value}]
    )

    joint_state_publisher_=Node(
        package="joint_state_publisher",
        executable="joint_state_publisher"
    )



    return LaunchDescription([robot_state_publisher_,joint_state_publisher_])
