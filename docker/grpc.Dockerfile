FROM grpc/python

COPY ./grpc /grpc

RUN pip install rio-tiler

ENTRYPOINT ["python", "/grpc/tile_server.py"]