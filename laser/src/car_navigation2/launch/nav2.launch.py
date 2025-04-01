import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node




def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true') 


    nav2_node=  IncludeLaunchDescription(
        PythonLaunchDescriptionSource(['/home/zjt/d2lros2/laser/install/nav2_bringup/share/nav2_bringup/launch/bringup_launch.py']),
        launch_arguments={
            'map':'/home/zjt/d2lros2/laser/install/car_navigation2/share/car_navigation2/maps/car2_map.yaml',
            'use_sim_time':use_sim_time,
            'params_file':'/home/zjt/d2lros2/laser/install/car_navigation2/share/car_navigation2/param/car_nav2.yaml'
        }.items(),
    )

    rviz2_node =Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=['-d', '/home/zjt/d2lros2/laser/install/nav2_bringup/share/nav2_bringup/rviz/nav2_default_view.rviz'],
        parameters=[{'use_sim_time': use_sim_time}],
         output='screen'
    )

    return LaunchDescription([nav2_node,rviz2_node])
