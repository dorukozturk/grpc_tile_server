# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tile_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tile_server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11tile_server.proto\"*\n\x07TileXYZ\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"\x14\n\x04Tile\x12\x0c\n\x04tile\x18\x01 \x01(\x0c\x32*\n\nTileServer\x12\x1c\n\x07GetTile\x12\x08.TileXYZ\x1a\x05.Tile\"\x00\x62\x06proto3')
)




_TILEXYZ = _descriptor.Descriptor(
  name='TileXYZ',
  full_name='TileXYZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='TileXYZ.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='TileXYZ.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='TileXYZ.z', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=63,
)


_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tile', full_name='Tile.tile', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=65,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['TileXYZ'] = _TILEXYZ
DESCRIPTOR.message_types_by_name['Tile'] = _TILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TileXYZ = _reflection.GeneratedProtocolMessageType('TileXYZ', (_message.Message,), {
  'DESCRIPTOR' : _TILEXYZ,
  '__module__' : 'tile_server_pb2'
  # @@protoc_insertion_point(class_scope:TileXYZ)
  })
_sym_db.RegisterMessage(TileXYZ)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), {
  'DESCRIPTOR' : _TILE,
  '__module__' : 'tile_server_pb2'
  # @@protoc_insertion_point(class_scope:Tile)
  })
_sym_db.RegisterMessage(Tile)



_TILESERVER = _descriptor.ServiceDescriptor(
  name='TileServer',
  full_name='TileServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=87,
  serialized_end=129,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTile',
    full_name='TileServer.GetTile',
    index=0,
    containing_service=None,
    input_type=_TILEXYZ,
    output_type=_TILE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TILESERVER)

DESCRIPTOR.services_by_name['TileServer'] = _TILESERVER

# @@protoc_insertion_point(module_scope)
