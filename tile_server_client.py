import logging

import grpc

import tile_server_pb2
import tile_server_pb2_grpc


def cog_get_tile(stub):
    TileXYZ = tile_server_pb2.TileXYZ(tiff_path="/data/data/cog/test.tif",
                                      x=38324, y=22089, z=16)
    return stub.GetTile(TileXYZ)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tile_server_pb2_grpc.TileServerStub(channel)
        cog_get_tile(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
