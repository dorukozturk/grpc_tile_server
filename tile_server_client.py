import logging

import grpc
from flask import Flask

import tile_server_pb2
import tile_server_pb2_grpc


app = Flask(__name__)


def cog_get_tile(stub, x, y, z):
    TileXYZ = tile_server_pb2.TileXYZ(tiff_path="/data/data/cog/test.tif",
                                      x=x, y=y, z=z)
    return stub.GetTile(TileXYZ)


@app.route('/<int:z>/<int:x>/<int:y>.png')
def serve_tiles(z, x, y):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tile_server_pb2_grpc.TileServerStub(channel)
        return cog_get_tile(stub, x, y, z).tile


if __name__ == '__main__':
    logging.basicConfig()
