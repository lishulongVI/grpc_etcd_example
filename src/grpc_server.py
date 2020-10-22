import grpc
from concurrent import futures
from protos import query_example_pb2_grpc
from protos import query_example_pb2


class ContactService(query_example_pb2_grpc.QueryService):
    def ContactSearch(self, request, context, **kwargs):
        print('accept msg:', request.name, request.phone)
        import time
        time.sleep(1)
        return query_example_pb2.ContactRes(id=1, addr='北京', contact=[
            query_example_pb2.ContactRes.Contact(name='张三', phone='10086'),
            query_example_pb2.ContactRes.Contact(name='张三', phone='10086'),
        ])


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100), options=[
        ('grpc.max_send_message_length', 1024 * 1024 * 1024),
        ('grpc.max_receive_message_length', 1024 * 1024 * 1024),
    ])

    query_example_pb2_grpc.add_QueryServiceServicer_to_server(ContactService(), server)
    server.add_insecure_port('[::]:3600')
    server.start()
    try:
        import time
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    server()
