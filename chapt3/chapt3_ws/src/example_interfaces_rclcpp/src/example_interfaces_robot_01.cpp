#include "rclcpp/rclcpp.hpp"
#include "example_ros2_interfaces/msg/robot_status.hpp"
#include "example_ros2_interfaces/srv/move_robot.hpp"
class Robot{
  public:
    Robot()=default;
    ~Robot()=default;

    float move_distance(float distance) {
    status_ = example_ros2_interfaces::msg::RobotStatus::STATUS_MOVEING;
    target_pose_ += distance;
    // 当目标距离和当前距离大于0.01则持续向目标移动
    while (fabs(target_pose_ - current_pose_) > 0.01) {
      // 每一步移动当前到目标距离的1/10
      float step = distance / fabs(distance) * fabs(target_pose_ - current_pose_) * 0.1;
      current_pose_ += step;
      std::cout << "移动了：" << step << "当前位置：" << current_pose_ << std::endl;
      // 当前线程休眠500ms
      std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    status_ = example_ros2_interfaces::msg::RobotStatus::STATUS_STOP;
    return current_pose_;
  }

  float get_current_pose() { return current_pose_; }


  int get_status() { return status_; }
  private:
    float current_pose_=0.0;
    float target_pose_=0.0;

    int status_=example_ros2_interfaces::msg::RobotStatus::STATUS_STOP;
};
class ExampleInterfacesRobot:public rclcpp::Node{
  public:
    ExampleInterfacesRobot(std::string name):Node(name){    
      RCLCPP_INFO(this->get_logger(),"节点：%s",name.c_str());
    

    move_robot_server_=this->create_service<example_ros2_interfaces::msg::RobotStatus>("move_robot",std::bind(&ExampleInterfacesRobot::handle_move_robot, this, std::placeholders::_1, std::placeholders::_2));
    robot_status_publisher_=this->create_publisher<example_ros2_interfaces::srv::MoveRobot>("robot_status",10);
    timer_=this->create_wall_timer(std::chrono::molliseconds(500),std::bind(&ExampleInterfacesRobot::timer_callback, this));

    }
    private:
      Robot robot;

      rclcpp::TimerBase::SharedPtr timer_;
      rclcpp::Publisher<example_ros2_interfaces::msg::RobotStatus>::SharedPtr robot_status_publisher_;
      rclcpp::Service<example_ros2_interfaces::srv::MoveRobot>::SharedPtr move_robot_server_;

      void timer_callback(){
        example_ros2_interfaces::msg::RobotStatus message;
        message.status=robot.get_status();
        message.pose=Robot.get_current_pose();
        RCLCPP_INFO(this->get_logger(), "Publishing: %f", robot.get_current_pose());
        robot_status_publisher_->publish(message);
      }

      void handle_move_robot(const std::shared_ptr<example_ros2_interfaces::srv::MoveRobot::Request> request,
                         std::shared_ptr<example_ros2_interfaces::srv::MoveRobot::Response> response){
        RCLCPP_INFO(this->get_logger(), "收到请求移动距离：%f，当前位置：%f", request->distance, robot.get_current_pose());
        robot.move_distance(request->distance);
        response->pose = robot.get_current_pose();

      }
};
int main(int argc, char ** argv)
{
  rclcpp::init(argc,argv);
  auto node = std::make_shared<ExampleInterfacesRobot>("example_interfaces_robot_01");
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
