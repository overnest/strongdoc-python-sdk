from strongdoc import client
from strongdoc.proto import search_pb2, strongdoc_pb2_grpc

def search(token, query):
    """
    Search for document that contains a specific word.
    
    :param token:
        The user JWT token.
    :type token:
        `string`
    :param query:
        The query string.
    :type query:
        `string`

    returns:
        The hit list of the search.
    :rtype:
        `Array` of :class:`DocumentResult`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request = search_pb2.SearchRequest(query=query)

        response = client_stub.Search(request)

        return response.hits
