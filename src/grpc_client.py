import grpc
import threading
from protos import query_example_pb2_grpc
from protos import query_example_pb2
from utils.pb import rpc_response2dict


class A(threading.Thread):
    def run(self) -> None:
        channel = grpc.insecure_channel('localhost:3600')
        stub = query_example_pb2_grpc.QueryServiceStub(channel)
        res = stub.ContactSearch(query_example_pb2.ContactReq(name='xxxx', phone='120'))
        # print(res)
        print(rpc_response2dict(res))


if __name__ == '__main__':
    for i in range(100):
        A().start()

    import time

    time.sleep(10)
