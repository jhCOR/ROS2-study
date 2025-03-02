import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from rclpy.executors import MultiThreadedExecutor  # 멀티 스레드 실행기 추가

from keyword_configuration import ADD_TWO_INTS_SERVER_NODE, ADD_TWO_INTS_SERVICE

class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__(ADD_TWO_INTS_SERVER_NODE)
        self.srv = self.create_service(AddTwoInts, ADD_TWO_INTS_SERVICE, self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        return response

def main():
    rclpy.init()
    node = AddTwoIntsServer()

    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
