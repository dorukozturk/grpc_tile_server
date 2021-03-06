# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import tile_server_pb2 as tile__server__pb2


class TileServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTile = channel.unary_unary(
        '/TileServer/GetTile',
        request_serializer=tile__server__pb2.TileXYZ.SerializeToString,
        response_deserializer=tile__server__pb2.Tile.FromString,
        )


class TileServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTile(self, request, context):
    """Simple RPC
    Obtains the tile at a given tile xyz
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TileServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTile': grpc.unary_unary_rpc_method_handler(
          servicer.GetTile,
          request_deserializer=tile__server__pb2.TileXYZ.FromString,
          response_serializer=tile__server__pb2.Tile.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TileServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
