import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorSimulator(Node):
    def __init__(self):
        # Initialize the ROS 2 Node with the name 'sensor_simulator'
        super().__init__('sensor_simulator')
        
        # Create a publisher that sends Float32 messages over the 'sensor/distance' topic
        self.publisher_ = self.create_publisher(Float32, 'sensor/distance', 10)
        
        # Create a timer that execution loops every 0.5 seconds
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('Sensor Simulator Node initialized.')

    def timer_callback(self):
        msg = Float32()
        # Generate a random float between 0.1m and 2.0m to simulate obstacles
        msg.data = random.uniform(0.1, 2.0)
        
        # Broadcast the message to any listening node
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)       # Initialize ROS 2 communications
    node = SensorSimulator()    # Instantiate the node class
    rclpy.spin(node)            # Keep the node alive and looping
    node.destroy_node()
    rclpy.shutdown()            # Cleanly shut down
