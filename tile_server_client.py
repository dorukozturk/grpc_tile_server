import logging

import grpc

import tile_server_pb2
import tile_server_pb2_grpc


def cog_get_tile(stub):
    TileXYZ = tile_server_pb2.TileXYZ(tiff_path="/data/data/cog/elevation.tif",
                                      x=0, y=0, z=0)
    return stub.GetTile(TileXYZ)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tile_server_pb2_grpc.TileServerStub(channel)
        print("-------------- GetTile --------------")
        cog_get_tile(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
