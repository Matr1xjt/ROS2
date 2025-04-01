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
        cmd=['gazebo', '--verbose','-s', 'libgazebo_ros_init.so', '-s','libgazebo_ros_factory.so'],#,'/home/zjt/d2lros2/laser/src/laser_nav2/world/myworld2.world'],
        output="both"
    )
    spawn_entity_cmd=Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments= ['-entity','car','-file',path],
        output="both"
    )

    """
    node=Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[("cloud_in",'/pointcloud_in'),
                        ('scan',  '/scan')],
            parameters=[{
                'target_frame': 'base_footprint',
                'transform_tolerance': 0.01,
                'min_height': 0,
                'max_height': 1,
                'angle_min': -1.5708,  # -M_PI/2
                'angle_max': 1.5708,  # M_PI/2    
                'angle_increment': 0.0087,  # M_PI/360.0s
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 4,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    """
    

    node =Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/pointcloud_in'),
                        ('scan', '/scan')],
            parameters=[{
                'target_frame': 'base_footprint',
                'transform_tolerance': 0.01,
                'min_height': 0.0,
                'max_height': 1.0,
                'angle_min': -3.14,  # -M_PI/2
                'angle_max': 3.14,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 10.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    
    tf_node=       Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=[
                '--x', '0', '--y', '0', '--z', '0',
                '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
                 #'--frame-id', 'map', '--child-frame-id', 'odom'
            ]
        )
    
    robot_state_publisher_=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        arguments=[path]
    )
    
    joint_state_publisher_=Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name='joint_state_publisher',
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time', default='true')}]
    )
    """
    rviz2_node=Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="both",
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time', default='true')}]
    )

    """

    return LaunchDescription([robot_state_publisher_,joint_state_publisher_,tf_node,start_gazebo_cmd,spawn_entity_cmd,node])#

#,robot_state_publisher_,joint_state_publisher_,rviz2_node
