import socket
import select
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GUIListenerNode(Node):
    def __init__(self):
        super().__init__('GUI_listener')

        # Declare and retrieve parameters
        self.declare_parameter('udp_ip', '127.0.0.1')
        self.declare_parameter('udp_port', 13303)
        udp_ip = self.get_parameter('udp_ip').get_parameter_value().string_value
        udp_port = self.get_parameter('udp_port').get_parameter_value().integer_value

        self.publisher_ = self.create_publisher(String, 'gui_data', 10)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((udp_ip, udp_port)) 
        self.sock.setblocking(0)
        self.read_list = [self.sock]
        self.timer = self.create_timer(0.05, self.timer_callback)

    def timer_callback(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            msg = String()
            msg.data = data.decode()
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
        except BlockingIOError:
            # No data available
            pass
        except Exception as e:
            self.get_logger().error(f"Error receiving data: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = GUIListenerNode() 
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
