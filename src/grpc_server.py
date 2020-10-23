import grpc
import threading
import time
from concurrent import futures
from protos import query_example_pb2_grpc
from protos import query_example_pb2
from src.etcd_service import EtcdService


class ContactService(query_example_pb2_grpc.QueryService):
    def ContactSearch(self, request, context, **kwargs):
        print('accept msg:', request.name, request.phone)
        import time
        time.sleep(1)
        return query_example_pb2.ContactRes(id=1, addr='北京', contact=[
            query_example_pb2.ContactRes.Contact(name='张三', phone='10086'),
            query_example_pb2.ContactRes.Contact(name='张三', phone='10086'),
        ])


class Register(threading.Thread):

    def __init__(self, stop=0):
        super().__init__()
        self.stop = stop

    def run(self) -> None:
        while 1 and self.stop == 0:
            time.sleep(1)
            EtcdService.register("/be-host/query_service", 'localhost:3600')


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100), options=[
        ('grpc.max_send_message_length', 1024 * 1024 * 1024),
        ('grpc.max_receive_message_length', 1024 * 1024 * 1024),
    ])

    query_example_pb2_grpc.add_QueryServiceServicer_to_server(ContactService(), server)
    server.add_insecure_port('[::]:3600')
    server.start()
    r = Register()
    r.start()
    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        r.stop = 1
        # 保证线程执行结束了
        time.sleep(1)
        EtcdService.un_register("/be-host/query_service")
        server.stop(0)


if __name__ == '__main__':
    server()
