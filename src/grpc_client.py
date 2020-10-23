import grpc
import threading
from protos import query_example_pb2_grpc
from protos import query_example_pb2
from utils.pb import rpc_response2dict

import logging
import etcd3

LOGGER = logging.getLogger(__file__)

client = etcd3.client('127.0.0.1', 2379)
ECD_CONFIG = {}


def watch_prefix_callback(event):
    """
    检测服务端的注册中心的变化，有变化的时候, 更新配置
    """
    for i in event.events:
        server_key = i.key.decode('U8')
        server_value = i.value.decode('U8')
        global ECD_CONFIG
        if not server_value:
            ECD_CONFIG.pop(server_key, None)
        else:
            ECD_CONFIG[server_key] = server_value
        print('etcd', ECD_CONFIG)


client.add_watch_prefix_callback('/', watch_prefix_callback)


class A(threading.Thread):
    def run(self) -> None:
        print(ECD_CONFIG)
        channel = grpc.insecure_channel(ECD_CONFIG.get('/be-host/query_service', 'localhost:3600'))
        stub = query_example_pb2_grpc.QueryServiceStub(channel)
        res = stub.ContactSearch(query_example_pb2.ContactReq(name='xxxx', phone='120'))
        print(rpc_response2dict(res))


if __name__ == '__main__':
    # 确保监听到配置文件
    while not ECD_CONFIG:
        pass

    for i in range(100):
        A().start()
    import time
    time.sleep(10000)
