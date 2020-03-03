from strongdoc import client
from strongdoc.proto import accounts_pb2, strongdoc_pb2_grpc

def login(userid, password, orgid):
    """
    Verify the user and organization identity, and returns a JWT token for future API use.

    :param userid:
       The login user ID
    :type userid:
        `string`
    :param password:
       The ogin user password
    :type password:
        `string`
    :param orgid:
       The login organization ID
    :type orgid:
        `string`
    :returns:
        The JWT token used to authenticate user/org when using StrongDoc APIs.
    :rtype:
        `string`
    """
    with client.connect_to_server_with_no_auth() as no_auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(no_auth_conn)

        # create login request message
        request = accounts_pb2.LoginRequest(userID=userid, password=password, orgID=orgid)

        # make the call
        response = client_stub.Login(request)
        
        return response.token
