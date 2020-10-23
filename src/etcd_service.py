import json
import logging
import etcd3

LOGGER = logging.getLogger(__file__)

client = etcd3.client('127.0.0.1', 2379)


# ECD_CONFIG = {}
#
#
# def watch_prefix_callback(event):
#     """
#     检测服务端的注册中心的变化，有变化的时候, 更新配置
#     """
#     for i in event.events:
#         server_key = i.key.decode('U8')
#         server_value = i.value.decode('U8')
#         if not server_value:
#             ECD_CONFIG.pop(server_key, None)
#         else:
#             ECD_CONFIG[server_key] = server_value
#         print(ECD_CONFIG)
#
#
# client.add_watch_prefix_callback('/', watch_prefix_callback)


class EtcdService:

    @classmethod
    def register(cls, key, value):
        client.put(key, value)

    @classmethod
    def un_register(cls, key):
        client.delete(key)

    @classmethod
    def get(cls, key):
        v, _ = client.get(key)
        return v.decode('U8')


if __name__ == '__main__':
    import time

    time.sleep(10000)
