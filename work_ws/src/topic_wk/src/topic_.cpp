
//topic_name:/turtle1/pose 
//topic_type:turtlesim/msg/Pose
/*
x: 0.0
y: 0.0
theta: 0.0
linear_velocity: 0.0
angular_velocity: 0.0
*/

//topic_name:/tf/turtle1/cmd_vel
//topic_type:geometry_msgs/msg/Twist
/*
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
*/
#include "geometry_msgs/msg/Twist.hpp"
#include "rclcpp/rclcpp.hpp"
#include "turtlesim/msg/pose.hpp"


class Turtle_Topic :public rclcpp::Node{
    public:
        Turtle_Topic():Node("topic_turtle"){
            RCLCPP_INFO(this->get_logger(), "节点");
            sub_=this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose ",10,std::bind(&Turtle_Topic::sub_callback,this,std::placeholders:_1));
            pub_=this->create_publisher<tf::turtlesim::msg::cmd_vel>("/tf/turtle1/cmd_vel",10);#topic_name
        }
    private:
        void sub_callback(turtlesim::msg::Pose pose){

            geometry_msgs::msg::Twist twist;
            twist.linear.x=pose.linear_velocity;
            twist.angular.z=-pose.angular_velocity;
            RCLCPP_INFO(this->get_logger(), "Publishing message");
            pub_->publish(twist);
        }
        rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr sub_;
        rclcpp::Publisher<geometry_msgs::msg::twist>::SharedPtr pub_;
};

int main(int argc,char**argv){
    rclcpp::init(argc,argv);
    node= std::make_shared<Turtle_Topic>("topic_turtle");
    rclcpp::spin(node);
    rclcpp::shutdowm()
}