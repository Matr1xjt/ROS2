#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
class TopicPublisher01:public rclcpp::Node
{
    public:
        TopicPublisher01(std::string name):Node(name){
            RCLCPP_INFO(this->get_logger(),"%s节点",name.c_str());
            command_publisher_=this->create_publisher<std_msgs::msg::String>("command",10);
            timer_=this->create_wall_timer(std::chrono::milliseconds(500),std::bind(&TopicPublisher01::timer_callback,this));
        }
    private:
        void timer_callback()
        {
            std_msgs::msg::String message;
            message.data="forward";

            RCLCPP_INFO(this->get_logger(),"Publisher:%s",message.data.c_str());

            command_publisher_->publish(message);
        }
        rclcpp::TimerBase::SharedPtr timer_;

        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr command_publisher_;

};
int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node=std::make_shared<TopicPublisher01>("topic_publisher_01");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}