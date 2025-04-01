import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node =Node("node_02")
    node.get_logger().info("node_02")
    rclpy.spin(node)
    rclpy.shutdown()
    
