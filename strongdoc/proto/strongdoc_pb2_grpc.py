# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import accounts_pb2 as accounts__pb2
import billing_pb2 as billing__pb2
import documentNoStore_pb2 as documentNoStore__pb2
import document_pb2 as document__pb2
import search_pb2 as search__pb2


class StrongDocServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterOrganization = channel.unary_unary(
        '/proto.StrongDocService/RegisterOrganization',
        request_serializer=accounts__pb2.RegisterOrganizationReq.SerializeToString,
        response_deserializer=accounts__pb2.RegisterOrganizationResp.FromString,
        )
    self.ReactivateOrganization = channel.unary_unary(
        '/proto.StrongDocService/ReactivateOrganization',
        request_serializer=accounts__pb2.RegisterOrganizationReq.SerializeToString,
        response_deserializer=accounts__pb2.RegisterOrganizationResp.FromString,
        )
    self.RemoveOrganization = channel.unary_unary(
        '/proto.StrongDocService/RemoveOrganization',
        request_serializer=accounts__pb2.RemoveOrganizationReq.SerializeToString,
        response_deserializer=accounts__pb2.RemoveOrganizationResp.FromString,
        )
    self.RegisterUser = channel.unary_unary(
        '/proto.StrongDocService/RegisterUser',
        request_serializer=accounts__pb2.RegisterUserReq.SerializeToString,
        response_deserializer=accounts__pb2.RegisterUserResp.FromString,
        )
    self.ListUsers = channel.unary_unary(
        '/proto.StrongDocService/ListUsers',
        request_serializer=accounts__pb2.ListUsersReq.SerializeToString,
        response_deserializer=accounts__pb2.ListUsersResp.FromString,
        )
    self.RemoveUser = channel.unary_unary(
        '/proto.StrongDocService/RemoveUser',
        request_serializer=accounts__pb2.RemoveUserReq.SerializeToString,
        response_deserializer=accounts__pb2.RemoveUserResp.FromString,
        )
    self.PromoteUser = channel.unary_unary(
        '/proto.StrongDocService/PromoteUser',
        request_serializer=accounts__pb2.PromoteUserReq.SerializeToString,
        response_deserializer=accounts__pb2.PromoteUserResp.FromString,
        )
    self.DemoteUser = channel.unary_unary(
        '/proto.StrongDocService/DemoteUser',
        request_serializer=accounts__pb2.DemoteUserReq.SerializeToString,
        response_deserializer=accounts__pb2.DemoteUserResp.FromString,
        )
    self.ListDocuments = channel.unary_unary(
        '/proto.StrongDocService/ListDocuments',
        request_serializer=document__pb2.ListDocumentsReq.SerializeToString,
        response_deserializer=document__pb2.ListDocumentsResp.FromString,
        )
    self.RemoveDocument = channel.unary_unary(
        '/proto.StrongDocService/RemoveDocument',
        request_serializer=document__pb2.RemoveDocumentReq.SerializeToString,
        response_deserializer=document__pb2.RemoveDocumentResp.FromString,
        )
    self.UploadDocumentStream = channel.stream_unary(
        '/proto.StrongDocService/UploadDocumentStream',
        request_serializer=document__pb2.UploadDocStreamReq.SerializeToString,
        response_deserializer=document__pb2.UploadDocStreamResp.FromString,
        )
    self.UploadDocument = channel.unary_unary(
        '/proto.StrongDocService/UploadDocument',
        request_serializer=document__pb2.UploadDocReq.SerializeToString,
        response_deserializer=document__pb2.UploadDocResp.FromString,
        )
    self.DownloadDocumentStream = channel.unary_stream(
        '/proto.StrongDocService/DownloadDocumentStream',
        request_serializer=document__pb2.DownloadDocStreamReq.SerializeToString,
        response_deserializer=document__pb2.DownloadDocStreamResp.FromString,
        )
    self.DownloadDocument = channel.unary_unary(
        '/proto.StrongDocService/DownloadDocument',
        request_serializer=document__pb2.DownloadDocReq.SerializeToString,
        response_deserializer=document__pb2.DownloadDocResp.FromString,
        )
    self.EncryptDocumentStream = channel.stream_stream(
        '/proto.StrongDocService/EncryptDocumentStream',
        request_serializer=documentNoStore__pb2.EncryptDocStreamReq.SerializeToString,
        response_deserializer=documentNoStore__pb2.EncryptDocStreamResp.FromString,
        )
    self.EncryptDocument = channel.unary_unary(
        '/proto.StrongDocService/EncryptDocument',
        request_serializer=documentNoStore__pb2.EncryptDocReq.SerializeToString,
        response_deserializer=documentNoStore__pb2.EncryptDocResp.FromString,
        )
    self.DecryptDocumentStream = channel.stream_stream(
        '/proto.StrongDocService/DecryptDocumentStream',
        request_serializer=documentNoStore__pb2.DecryptDocStreamReq.SerializeToString,
        response_deserializer=documentNoStore__pb2.DecryptDocStreamResp.FromString,
        )
    self.DecryptDocument = channel.unary_unary(
        '/proto.StrongDocService/DecryptDocument',
        request_serializer=documentNoStore__pb2.DecryptDocReq.SerializeToString,
        response_deserializer=documentNoStore__pb2.DecryptDocResp.FromString,
        )
    self.ShareDocument = channel.unary_unary(
        '/proto.StrongDocService/ShareDocument',
        request_serializer=document__pb2.ShareDocumentReq.SerializeToString,
        response_deserializer=document__pb2.ShareDocumentResp.FromString,
        )
    self.UnshareDocument = channel.unary_unary(
        '/proto.StrongDocService/UnshareDocument',
        request_serializer=document__pb2.UnshareDocumentReq.SerializeToString,
        response_deserializer=document__pb2.UnshareDocumentResp.FromString,
        )
    self.Login = channel.unary_unary(
        '/proto.StrongDocService/Login',
        request_serializer=accounts__pb2.LoginReq.SerializeToString,
        response_deserializer=accounts__pb2.LoginResp.FromString,
        )
    self.Logout = channel.unary_unary(
        '/proto.StrongDocService/Logout',
        request_serializer=accounts__pb2.LogoutReq.SerializeToString,
        response_deserializer=accounts__pb2.LogoutResp.FromString,
        )
    self.Search = channel.unary_unary(
        '/proto.StrongDocService/Search',
        request_serializer=search__pb2.SearchReq.SerializeToString,
        response_deserializer=search__pb2.SearchResp.FromString,
        )
    self.AddSharableOrg = channel.unary_unary(
        '/proto.StrongDocService/AddSharableOrg',
        request_serializer=accounts__pb2.AddSharableOrgReq.SerializeToString,
        response_deserializer=accounts__pb2.AddSharableOrgResp.FromString,
        )
    self.RemoveSharableOrg = channel.unary_unary(
        '/proto.StrongDocService/RemoveSharableOrg',
        request_serializer=accounts__pb2.RemoveSharableOrgReq.SerializeToString,
        response_deserializer=accounts__pb2.RemoveSharableOrgResp.FromString,
        )
    self.SetMultiLevelSharing = channel.unary_unary(
        '/proto.StrongDocService/SetMultiLevelSharing',
        request_serializer=accounts__pb2.SetMultiLevelSharingReq.SerializeToString,
        response_deserializer=accounts__pb2.SetMultiLevelSharingResp.FromString,
        )
    self.SetAccountInfo = channel.unary_unary(
        '/proto.StrongDocService/SetAccountInfo',
        request_serializer=accounts__pb2.SetAccountInfoReq.SerializeToString,
        response_deserializer=accounts__pb2.SetAccountInfoResp.FromString,
        )
    self.GetBillingDetails = channel.unary_unary(
        '/proto.StrongDocService/GetBillingDetails',
        request_serializer=billing__pb2.GetBillingDetailsReq.SerializeToString,
        response_deserializer=billing__pb2.GetBillingDetailsResp.FromString,
        )
    self.GetBillingFrequencyList = channel.unary_unary(
        '/proto.StrongDocService/GetBillingFrequencyList',
        request_serializer=billing__pb2.GetBillingFrequencyListReq.SerializeToString,
        response_deserializer=billing__pb2.GetBillingFrequencyListResp.FromString,
        )
    self.SetNextBillingFrequency = channel.unary_unary(
        '/proto.StrongDocService/SetNextBillingFrequency',
        request_serializer=billing__pb2.SetNextBillingFrequencyReq.SerializeToString,
        response_deserializer=billing__pb2.SetNextBillingFrequencyResp.FromString,
        )
    self.GetLargeTraffic = channel.unary_unary(
        '/proto.StrongDocService/GetLargeTraffic',
        request_serializer=billing__pb2.GetLargeTrafficReq.SerializeToString,
        response_deserializer=billing__pb2.GetLargeTrafficResp.FromString,
        )
    self.GetAccountInfo = channel.unary_unary(
        '/proto.StrongDocService/GetAccountInfo',
        request_serializer=accounts__pb2.GetAccountInfoReq.SerializeToString,
        response_deserializer=accounts__pb2.GetAccountInfoResp.FromString,
        )
    self.GetUserInfo = channel.unary_unary(
        '/proto.StrongDocService/GetUserInfo',
        request_serializer=accounts__pb2.GetUserInfoReq.SerializeToString,
        response_deserializer=accounts__pb2.GetUserInfoResp.FromString,
        )
    self.ChangeUserPassword = channel.unary_unary(
        '/proto.StrongDocService/ChangeUserPassword',
        request_serializer=accounts__pb2.ChangeUserPasswordReq.SerializeToString,
        response_deserializer=accounts__pb2.ChangeUserPasswordResp.FromString,
        )
    self.SetUserInfo = channel.unary_unary(
        '/proto.StrongDocService/SetUserInfo',
        request_serializer=accounts__pb2.SetUserInfoReq.SerializeToString,
        response_deserializer=accounts__pb2.SetUserInfoResp.FromString,
        )
    self.ListCreditCards = channel.unary_unary(
        '/proto.StrongDocService/ListCreditCards',
        request_serializer=billing__pb2.ListCreditCardsReq.SerializeToString,
        response_deserializer=billing__pb2.ListCreditCardsResp.FromString,
        )
    self.AddPaymentMethod = channel.unary_unary(
        '/proto.StrongDocService/AddPaymentMethod',
        request_serializer=billing__pb2.AddPaymentMethodReq.SerializeToString,
        response_deserializer=billing__pb2.AddPaymentMethodResp.FromString,
        )
    self.SetDefaultPaymentMethod = channel.unary_unary(
        '/proto.StrongDocService/SetDefaultPaymentMethod',
        request_serializer=billing__pb2.SetDefaultPaymentMethodReq.SerializeToString,
        response_deserializer=billing__pb2.SetDefaultPaymentMethodResp.FromString,
        )
    self.RemovePaymentMethod = channel.unary_unary(
        '/proto.StrongDocService/RemovePaymentMethod',
        request_serializer=billing__pb2.RemovePaymentMethodReq.SerializeToString,
        response_deserializer=billing__pb2.RemovePaymentMethodResp.FromString,
        )


class StrongDocServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterOrganization(self, request, context):
    """Registers a new organization

    The user who created the organization is automatically an administrator

    Does not require Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReactivateOrganization(self, request, context):
    """Reactivate an organization that was unsubscribed via aws

    The user reactivating the organization becomes the administrator

    Does not require login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveOrganization(self, request, context):
    """Remove an organization and its search indexes

    Requires Administrator privilege. Only an administrator can remove the whole organization

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterUser(self, request, context):
    """Register new user

    Creates new user if it doesn't already exist. If the user already exist, and
    error is thrown

    Requires administrator privilege
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUsers(self, request, context):
    """rpc GetUserInfo(GetUserInfoReq) returns (GetUserInfoResp) {
    option (google.api.http) = {
    post: "/v1/account/getuserinfo"
    body: "*"
    };
    option (grpc.gateway.protoc_gen_swagger.options.openapiv2_operation) = {
    security: {
    security_requirement: {
    key: "ApiKeyAuth";
    value: {};
    }
    };
    };
    }

    List the users of the organization

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveUser(self, request, context):
    """Remove user from organization

    Removes the user from the organization. The users documents still exists,
    but belong to the organization, only accessible by organization admin.

    Requires administrator privilege.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PromoteUser(self, request, context):
    """Promote a regular user to administrator at the organization

    Requires administrator privilege.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DemoteUser(self, request, context):
    """Demote administrator to regular user at the organization. Attempting to
    demote the last administrator of an organization will fail

    Requires administrator privilege.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDocuments(self, request, context):
    """List the documents the user can access

    Administrators can see all documents belonging to the organization

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveDocument(self, request, context):
    """Remove document the user can access

    Admin user can remove document for the whole organization
    Regular user only can remove document for him/herself

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadDocumentStream(self, request_iterator, context):
    """Upload document

    User can upload document to the organization for storage

    Requires Login
    This is not available through gRPC REST gateway,
    since REST api does not support streaming protocol
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadDocument(self, request, context):
    """Upload document

    User can upload document to the organization for storage

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadDocumentStream(self, request, context):
    """Download document stream

    User can download the documents

    Requires Login
    This is not available through gRPC REST gateway,
    since REST api does not support streaming protocol
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadDocument(self, request, context):
    """Download document

    User can download the documents

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EncryptDocumentStream(self, request_iterator, context):
    """Encrypt document stream encrypts the document and returns the ciphertext
    back to the user without storing it.

    Requires Login
    This is not available through gRPC REST gateway,
    since REST api does not support streaming protocol
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EncryptDocument(self, request, context):
    """Encrypt document encrypts the document and returns the ciphertext
    back to the user without storing it.

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecryptDocumentStream(self, request_iterator, context):
    """Decrypt document stream decrypts the ciphertext passed in and returns
    decrypted plain text back to the user without storing it

    Requires Login
    This is not available through gRPC REST gateway,
    since REST api does not support streaming protocol
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecryptDocument(self, request, context):
    """Decrypt document decrypts the ciphertext passed in and returns
    decrypted plain text back to the user without storing it
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShareDocument(self, request, context):
    """Share a document to another user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnshareDocument(self, request, context):
    """Unshare a document that had previously been shared to a user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Login(self, request, context):
    """Obtain an authentication token to be used with other APIs

    An authentication token will be returned after user has been validated
    The returned token will be used as a Bearer Token and need to be set in
    the request header
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Logout(self, request, context):
    """Logout current user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Search(self, request, context):
    """Search within a list of user's accessible documents

    The response will include a list document id and its score when matches are found

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddSharableOrg(self, request, context):
    """Add a sharable organization to the user's organization.

    Requires Administrator privilege.
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveSharableOrg(self, request, context):
    """Remove a sharable organization from the user's organization.

    Requires Administrator privilege.
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetMultiLevelSharing(self, request, context):
    """Update the organization's multi-level sharing setting

    Requires Administrator privilege.
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetAccountInfo(self, request, context):
    """Update the organization's account info

    Requires Administrator privilege.
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBillingDetails(self, request, context):
    """List all items of the cost breakdown and also other details such as the billing frequency

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBillingFrequencyList(self, request, context):
    """Obtain the list of billing frequencies (past, current and future)

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetNextBillingFrequency(self, request, context):
    """Change the next billing frequency

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLargeTraffic(self, request, context):
    """Obtain the list of large traffic usages

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAccountInfo(self, request, context):
    """Obtain information about the account

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserInfo(self, request, context):
    """Obtain information about logged in user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeUserPassword(self, request, context):
    """Change the password of a logged in user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetUserInfo(self, request, context):
    """Set information about a logged in user

    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCreditCards(self, request, context):
    """Obtain a list of the org's credit cards

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPaymentMethod(self, request, context):
    """Add a payment method to the customer and validate the payment method

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDefaultPaymentMethod(self, request, context):
    """Set the default payment method for a stripe customer

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemovePaymentMethod(self, request, context):
    """Remove a payment method for a stripe customer

    Requires Administrator privilege
    Requires Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StrongDocServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterOrganization,
          request_deserializer=accounts__pb2.RegisterOrganizationReq.FromString,
          response_serializer=accounts__pb2.RegisterOrganizationResp.SerializeToString,
      ),
      'ReactivateOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.ReactivateOrganization,
          request_deserializer=accounts__pb2.RegisterOrganizationReq.FromString,
          response_serializer=accounts__pb2.RegisterOrganizationResp.SerializeToString,
      ),
      'RemoveOrganization': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveOrganization,
          request_deserializer=accounts__pb2.RemoveOrganizationReq.FromString,
          response_serializer=accounts__pb2.RemoveOrganizationResp.SerializeToString,
      ),
      'RegisterUser': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterUser,
          request_deserializer=accounts__pb2.RegisterUserReq.FromString,
          response_serializer=accounts__pb2.RegisterUserResp.SerializeToString,
      ),
      'ListUsers': grpc.unary_unary_rpc_method_handler(
          servicer.ListUsers,
          request_deserializer=accounts__pb2.ListUsersReq.FromString,
          response_serializer=accounts__pb2.ListUsersResp.SerializeToString,
      ),
      'RemoveUser': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveUser,
          request_deserializer=accounts__pb2.RemoveUserReq.FromString,
          response_serializer=accounts__pb2.RemoveUserResp.SerializeToString,
      ),
      'PromoteUser': grpc.unary_unary_rpc_method_handler(
          servicer.PromoteUser,
          request_deserializer=accounts__pb2.PromoteUserReq.FromString,
          response_serializer=accounts__pb2.PromoteUserResp.SerializeToString,
      ),
      'DemoteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DemoteUser,
          request_deserializer=accounts__pb2.DemoteUserReq.FromString,
          response_serializer=accounts__pb2.DemoteUserResp.SerializeToString,
      ),
      'ListDocuments': grpc.unary_unary_rpc_method_handler(
          servicer.ListDocuments,
          request_deserializer=document__pb2.ListDocumentsReq.FromString,
          response_serializer=document__pb2.ListDocumentsResp.SerializeToString,
      ),
      'RemoveDocument': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveDocument,
          request_deserializer=document__pb2.RemoveDocumentReq.FromString,
          response_serializer=document__pb2.RemoveDocumentResp.SerializeToString,
      ),
      'UploadDocumentStream': grpc.stream_unary_rpc_method_handler(
          servicer.UploadDocumentStream,
          request_deserializer=document__pb2.UploadDocStreamReq.FromString,
          response_serializer=document__pb2.UploadDocStreamResp.SerializeToString,
      ),
      'UploadDocument': grpc.unary_unary_rpc_method_handler(
          servicer.UploadDocument,
          request_deserializer=document__pb2.UploadDocReq.FromString,
          response_serializer=document__pb2.UploadDocResp.SerializeToString,
      ),
      'DownloadDocumentStream': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadDocumentStream,
          request_deserializer=document__pb2.DownloadDocStreamReq.FromString,
          response_serializer=document__pb2.DownloadDocStreamResp.SerializeToString,
      ),
      'DownloadDocument': grpc.unary_unary_rpc_method_handler(
          servicer.DownloadDocument,
          request_deserializer=document__pb2.DownloadDocReq.FromString,
          response_serializer=document__pb2.DownloadDocResp.SerializeToString,
      ),
      'EncryptDocumentStream': grpc.stream_stream_rpc_method_handler(
          servicer.EncryptDocumentStream,
          request_deserializer=documentNoStore__pb2.EncryptDocStreamReq.FromString,
          response_serializer=documentNoStore__pb2.EncryptDocStreamResp.SerializeToString,
      ),
      'EncryptDocument': grpc.unary_unary_rpc_method_handler(
          servicer.EncryptDocument,
          request_deserializer=documentNoStore__pb2.EncryptDocReq.FromString,
          response_serializer=documentNoStore__pb2.EncryptDocResp.SerializeToString,
      ),
      'DecryptDocumentStream': grpc.stream_stream_rpc_method_handler(
          servicer.DecryptDocumentStream,
          request_deserializer=documentNoStore__pb2.DecryptDocStreamReq.FromString,
          response_serializer=documentNoStore__pb2.DecryptDocStreamResp.SerializeToString,
      ),
      'DecryptDocument': grpc.unary_unary_rpc_method_handler(
          servicer.DecryptDocument,
          request_deserializer=documentNoStore__pb2.DecryptDocReq.FromString,
          response_serializer=documentNoStore__pb2.DecryptDocResp.SerializeToString,
      ),
      'ShareDocument': grpc.unary_unary_rpc_method_handler(
          servicer.ShareDocument,
          request_deserializer=document__pb2.ShareDocumentReq.FromString,
          response_serializer=document__pb2.ShareDocumentResp.SerializeToString,
      ),
      'UnshareDocument': grpc.unary_unary_rpc_method_handler(
          servicer.UnshareDocument,
          request_deserializer=document__pb2.UnshareDocumentReq.FromString,
          response_serializer=document__pb2.UnshareDocumentResp.SerializeToString,
      ),
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=accounts__pb2.LoginReq.FromString,
          response_serializer=accounts__pb2.LoginResp.SerializeToString,
      ),
      'Logout': grpc.unary_unary_rpc_method_handler(
          servicer.Logout,
          request_deserializer=accounts__pb2.LogoutReq.FromString,
          response_serializer=accounts__pb2.LogoutResp.SerializeToString,
      ),
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=search__pb2.SearchReq.FromString,
          response_serializer=search__pb2.SearchResp.SerializeToString,
      ),
      'AddSharableOrg': grpc.unary_unary_rpc_method_handler(
          servicer.AddSharableOrg,
          request_deserializer=accounts__pb2.AddSharableOrgReq.FromString,
          response_serializer=accounts__pb2.AddSharableOrgResp.SerializeToString,
      ),
      'RemoveSharableOrg': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveSharableOrg,
          request_deserializer=accounts__pb2.RemoveSharableOrgReq.FromString,
          response_serializer=accounts__pb2.RemoveSharableOrgResp.SerializeToString,
      ),
      'SetMultiLevelSharing': grpc.unary_unary_rpc_method_handler(
          servicer.SetMultiLevelSharing,
          request_deserializer=accounts__pb2.SetMultiLevelSharingReq.FromString,
          response_serializer=accounts__pb2.SetMultiLevelSharingResp.SerializeToString,
      ),
      'SetAccountInfo': grpc.unary_unary_rpc_method_handler(
          servicer.SetAccountInfo,
          request_deserializer=accounts__pb2.SetAccountInfoReq.FromString,
          response_serializer=accounts__pb2.SetAccountInfoResp.SerializeToString,
      ),
      'GetBillingDetails': grpc.unary_unary_rpc_method_handler(
          servicer.GetBillingDetails,
          request_deserializer=billing__pb2.GetBillingDetailsReq.FromString,
          response_serializer=billing__pb2.GetBillingDetailsResp.SerializeToString,
      ),
      'GetBillingFrequencyList': grpc.unary_unary_rpc_method_handler(
          servicer.GetBillingFrequencyList,
          request_deserializer=billing__pb2.GetBillingFrequencyListReq.FromString,
          response_serializer=billing__pb2.GetBillingFrequencyListResp.SerializeToString,
      ),
      'SetNextBillingFrequency': grpc.unary_unary_rpc_method_handler(
          servicer.SetNextBillingFrequency,
          request_deserializer=billing__pb2.SetNextBillingFrequencyReq.FromString,
          response_serializer=billing__pb2.SetNextBillingFrequencyResp.SerializeToString,
      ),
      'GetLargeTraffic': grpc.unary_unary_rpc_method_handler(
          servicer.GetLargeTraffic,
          request_deserializer=billing__pb2.GetLargeTrafficReq.FromString,
          response_serializer=billing__pb2.GetLargeTrafficResp.SerializeToString,
      ),
      'GetAccountInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetAccountInfo,
          request_deserializer=accounts__pb2.GetAccountInfoReq.FromString,
          response_serializer=accounts__pb2.GetAccountInfoResp.SerializeToString,
      ),
      'GetUserInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserInfo,
          request_deserializer=accounts__pb2.GetUserInfoReq.FromString,
          response_serializer=accounts__pb2.GetUserInfoResp.SerializeToString,
      ),
      'ChangeUserPassword': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeUserPassword,
          request_deserializer=accounts__pb2.ChangeUserPasswordReq.FromString,
          response_serializer=accounts__pb2.ChangeUserPasswordResp.SerializeToString,
      ),
      'SetUserInfo': grpc.unary_unary_rpc_method_handler(
          servicer.SetUserInfo,
          request_deserializer=accounts__pb2.SetUserInfoReq.FromString,
          response_serializer=accounts__pb2.SetUserInfoResp.SerializeToString,
      ),
      'ListCreditCards': grpc.unary_unary_rpc_method_handler(
          servicer.ListCreditCards,
          request_deserializer=billing__pb2.ListCreditCardsReq.FromString,
          response_serializer=billing__pb2.ListCreditCardsResp.SerializeToString,
      ),
      'AddPaymentMethod': grpc.unary_unary_rpc_method_handler(
          servicer.AddPaymentMethod,
          request_deserializer=billing__pb2.AddPaymentMethodReq.FromString,
          response_serializer=billing__pb2.AddPaymentMethodResp.SerializeToString,
      ),
      'SetDefaultPaymentMethod': grpc.unary_unary_rpc_method_handler(
          servicer.SetDefaultPaymentMethod,
          request_deserializer=billing__pb2.SetDefaultPaymentMethodReq.FromString,
          response_serializer=billing__pb2.SetDefaultPaymentMethodResp.SerializeToString,
      ),
      'RemovePaymentMethod': grpc.unary_unary_rpc_method_handler(
          servicer.RemovePaymentMethod,
          request_deserializer=billing__pb2.RemovePaymentMethodReq.FromString,
          response_serializer=billing__pb2.RemovePaymentMethodResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.StrongDocService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
