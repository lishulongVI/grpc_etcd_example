from google.protobuf.descriptor import FieldDescriptor


def rpc_response2dict(response):
    """
    gRPC protocol buffer 对象序列化
    """
    result = {}
    if not response.IsInitialized():
        return None
    for field in response.DESCRIPTOR.fields:
        # 对齐结构
        # if not getattr(response, field.name):
        #     continue
        if not field.label == FieldDescriptor.LABEL_REPEATED:
            if not field.type == FieldDescriptor.TYPE_MESSAGE:
                result[field.name] = getattr(response, field.name)
            else:
                value = rpc_response2dict(getattr(response, field.name))
                if value:
                    result[field.name] = value
        else:
            if field.type == FieldDescriptor.TYPE_MESSAGE:
                result[field.name] = [rpc_response2dict(v) for v in getattr(response, field.name)]
            else:
                result[field.name] = [v for v in getattr(response, field.name)]
    return result
