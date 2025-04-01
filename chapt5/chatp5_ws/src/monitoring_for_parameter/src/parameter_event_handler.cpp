#include "rclcpp/rclcpp.hpp"

class Param :public rclcpp::Node{
    public:
        Param():Node("node_with_parameters"){
            this->declare_parameter("an_int_param",0);

            Param_subscriber_=std::make_shared<rclcpp::ParameterEventHandler>(this);
            
            auto cb =[this](const rclcpp::Parameter &p){
                RCLCPP_INFO(
                    this->get_logger(), "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
                    p.get_name().c_str(),
                    p.get_type_name().c_str(),
                    p.as_int());
                
            };
            
        
            cb_handle_ = Param_subscriber_->add_parameter_callback("an_int_param",cb);
        }

    private:
        std::shared_ptr<rclcpp::ParameterEventHandler> Param_subscriber_;
        std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
                                
};

int main(int argc , char** argv){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Param>());
    rclcpp::shutdown();
    return 0;
}