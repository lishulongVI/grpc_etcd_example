# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/query_example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/query_example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aprotos/query_example.proto\")\n\nContactReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05phone\x18\x02 \x01(\t\"t\n\nContactRes\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12$\n\x07\x63ontact\x18\x03 \x03(\x0b\x32\x13.ContactRes.Contact\x1a&\n\x07\x43ontact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05phone\x18\x02 \x01(\t29\n\x0cQueryService\x12)\n\rContactSearch\x12\x0b.ContactReq\x1a\x0b.ContactResb\x06proto3'
)




_CONTACTREQ = _descriptor.Descriptor(
  name='ContactReq',
  full_name='ContactReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ContactReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone', full_name='ContactReq.phone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=71,
)


_CONTACTRES_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='ContactRes.Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ContactRes.Contact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone', full_name='ContactRes.Contact.phone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=189,
)

_CONTACTRES = _descriptor.Descriptor(
  name='ContactRes',
  full_name='ContactRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ContactRes.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addr', full_name='ContactRes.addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contact', full_name='ContactRes.contact', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTACTRES_CONTACT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=189,
)

_CONTACTRES_CONTACT.containing_type = _CONTACTRES
_CONTACTRES.fields_by_name['contact'].message_type = _CONTACTRES_CONTACT
DESCRIPTOR.message_types_by_name['ContactReq'] = _CONTACTREQ
DESCRIPTOR.message_types_by_name['ContactRes'] = _CONTACTRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContactReq = _reflection.GeneratedProtocolMessageType('ContactReq', (_message.Message,), {
  'DESCRIPTOR' : _CONTACTREQ,
  '__module__' : 'protos.query_example_pb2'
  # @@protoc_insertion_point(class_scope:ContactReq)
  })
_sym_db.RegisterMessage(ContactReq)

ContactRes = _reflection.GeneratedProtocolMessageType('ContactRes', (_message.Message,), {

  'Contact' : _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
    'DESCRIPTOR' : _CONTACTRES_CONTACT,
    '__module__' : 'protos.query_example_pb2'
    # @@protoc_insertion_point(class_scope:ContactRes.Contact)
    })
  ,
  'DESCRIPTOR' : _CONTACTRES,
  '__module__' : 'protos.query_example_pb2'
  # @@protoc_insertion_point(class_scope:ContactRes)
  })
_sym_db.RegisterMessage(ContactRes)
_sym_db.RegisterMessage(ContactRes.Contact)



_QUERYSERVICE = _descriptor.ServiceDescriptor(
  name='QueryService',
  full_name='QueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=191,
  serialized_end=248,
  methods=[
  _descriptor.MethodDescriptor(
    name='ContactSearch',
    full_name='QueryService.ContactSearch',
    index=0,
    containing_service=None,
    input_type=_CONTACTREQ,
    output_type=_CONTACTRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE)

DESCRIPTOR.services_by_name['QueryService'] = _QUERYSERVICE

# @@protoc_insertion_point(module_scope)
