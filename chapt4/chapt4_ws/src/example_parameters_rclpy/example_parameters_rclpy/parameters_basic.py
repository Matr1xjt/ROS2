import rclpy
from rclpy.node import Node

class ParametersBasicNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("节点:%s"%name)

        self.declare_parameter('rcl_log_level',0)

        log_level=self.get_parameter("rcl_log_level").value

        self.get_logger.set_level(log_level)

        self.timer=self.create_timer(0.5,self.timer_callback)
    def timer_callback(self):
        log_level=self.get_parameter("rcl_log_level").value
        self.get_logger.set_level(log_level)

        print(f"========================{log_level}=============================")
        self.get_logger().debug("我是DEBUG级别的日志，我被打印出来了!")
        self.get_logger().info("我是INFO级别的日志，我被打印出来了!")
        self.get_logger().warn("我是WARN级别的日志，我被打印出来了!")
        self.get_logger().error("我是ERROR级别的日志，我被打印出来了!")
        self.get_logger().fatal("我是FATAL级别的日志，我被打印出来了!")
def main(args=None):
    rclpy.init(args=args)
    node =ParametersBasicNode("parameters_basic")
    rclpy.spin(node)
    rclpy.shutdown()
    