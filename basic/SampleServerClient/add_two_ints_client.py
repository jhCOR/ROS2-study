import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

from keyword_configuration import ADD_TWO_INTS_CLIENT_NODE, ADD_TWO_INTS_SERVICE

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__(ADD_TWO_INTS_CLIENT_NODE)
        self.cli = self.create_client(AddTwoInts, ADD_TWO_INTS_SERVICE)

        # 🔹 서비스가 준비될 때까지 대기
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service to become available...')
        
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()
    node = AddTwoIntsClient()
    response = node.send_request(5, 10)
    print(f"Result: {response.sum}")
    rclpy.shutdown()

if __name__ == '__main__':
    print("Start AddTwoIntsClient")
    main()

