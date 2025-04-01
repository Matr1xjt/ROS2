import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class NodeSubscribe02(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s"%name)

        self.command_subscribe_=self.create_subscription(String,"command",self.command_callback,10)
    
    def command_callback(self,msg):
        speed=0.0
        if msg.data == "backup":
            speed =-0.2
        self.get_logger().info(f'收到[{msg.data}],速度{speed}')

def main(args=None):
    rclpy.init(args=args)
    node = NodeSubscribe02("topic_subscribe_02")
    rclpy.spin(node)
    rclpy.shutdown()