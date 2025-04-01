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
    """
    p_value= ParameterValue(Command(["xacro ",get_package_share_directory("cpp06_urdf") + "/urdf/urdf/h01.urdf"]))#构建对象——————————command(命令行)————————————————get_package_share_directory()得到路径
    """
    model=DeclareLaunchArgument(name="model",default_value="h01.urdf")#设置参数

    p_value= ParameterValue(Command(["xacro "+get_package_share_directory("cpp06_urdf")+"/urdf/urdf/" ,LaunchConfiguration("model")]))
    robot_state_pub =Node(package="robot_state_publisher",
                          executable="robot_state_publisher",
                          parameters=[{"robot_description":p_value}])#对象

    joint_state_pub =Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
    )

    rviz2=Node(package="rviz2",
               executable="rviz2",

               arguments=["-d",get_package_share_directory("cpp06_urdf")+"/rviz/urdf.rviz"]#使用已经保存的rviz配置文件

               )

    return LaunchDescription([model,robot_state_pub,joint_state_pub,rviz2])
#参数调用格式
#ros2 launch cpp06_urdf display.launch.py model:=`ros2 pkg prefix --share cpp06_urdf`/urdf/urdf/h02.urdf