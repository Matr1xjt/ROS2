import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
import launch_ros
from launch_ros.substitutions import FindPackageShare
def generate_launch_description():
    path='/home/zjt/d2lros2/laser/install/laser_nav2/share/laser_nav2/urdf/car.urdf'
    start_gazebo_cmd=ExecuteProcess(
        cmd=['gazebo', '--verbose','-s', 'libgazebo_ros_init.so', '-s','libgazebo_ros_factory.so','/home/zjt/d2lros2/laser/src/laser_nav2/world/myworld2.world'],
        output="both"
    )
    spawn_entity_cmd=Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments= ['-entity','car','-file',path],
        output="both"
    )

    return LaunchDescription([start_gazebo_cmd,spawn_entity_cmd])


