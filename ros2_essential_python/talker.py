import rclpy 
from rclpy.node import Node
from std_msgs.msg import String 

class TalkerPublisher(Node):

    def __init__(self):
        super().__init__('talker_publisher')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        timer_period = 2 # 0.5 Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter=0

    def timer_callback(self):
        msg=String()
        msg.data = 'Hello World: %d' %self.counter
        self.publisher.publish(msg)
        self.counter=self.counter+1
        #print('Publishing" ', msg.data, '')
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main (args=None):

        rclpy.init(args=args)
        talker_publisher = TalkerPublisher()

        rclpy.spin(talker_publisher)

        talker_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

        
