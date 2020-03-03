from os import path

"""
Location of StrongDoc Service
"""
HOST = 'localhost'  # UPDATE TO USE api.strongsalt.com
PORT = 9090
CERT = path.join(path.dirname(__file__), "data", "certs", "grpc.root.localhost.pem")  # UPDATE TO USE grpc.root.pem`

"""
Timeout value for the gRPC connection
"""
GRPC_TIMEOUT = 60
