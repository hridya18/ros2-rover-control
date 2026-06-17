import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class RoverBrain(Node):
    def __init__(self):
        super().__init__('rover_brain')
        
        # Subscribe to the 'sensor/distance' topic to receive data from our simulator
        self.subscription = self.create_subscription(
            Float32,
            'sensor/distance',
            self.listener_callback,
            10) # 10 is the Queue Size (QoS historical depth limit)
            
        # Create a new publisher to send text alerts over 'motor/command'
        self.publisher_ = self.create_publisher(String, 'motor/command', 10)
        self.get_logger().info('Rover Brain Node initialized.')

    def listener_callback(self, msg):
        distance = msg.data
        command = String()
        
        # Core Decision Logic
        if distance < 0.5:
            command.data = f"CRITICAL: Obstacle at {distance:.2f}m! Turning LEFT."
            self.get_logger().warn(command.data)
        else:
            command.data = f"Clear path ({distance:.2f}m). Moving FORWARD."
            self.get_logger().info(command.data)
            
        # Publish the finalized decision
        self.publisher_.publish(command)

def main(args=None):
    rclpy.init(args=args)
    node = RoverBrain()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
