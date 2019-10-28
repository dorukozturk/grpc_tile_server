FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY grpc /app

RUN pip install grpcio protobuf

RUN mv /app/tile_server_client.py /app/main.py