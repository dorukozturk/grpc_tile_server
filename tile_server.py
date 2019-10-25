from concurrent import futures
import logging

import grpc
from rio_tiler import main
from rio_tiler.utils import array_to_image

import tile_server_pb2_grpc


def get_tile(path, x, y, z):
    tile, mask = main.tile(path, x, y, z, tilesize=256)
    return array_to_image(tile, mask=mask)


class TileServerServicer(tile_server_pb2_grpc.TileServerServicer):
    def GetTile(self, request, context):
        return get_tile(request.tiff_path,
                        request.x,
                        request.y,
                        request.z)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tile_server_pb2_grpc.add_TileServerServicer_to_server(
        TileServerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()