# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strongdoc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from strongdoc.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from strongdoc.proto.protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
import document_pb2 as document__pb2
import documentNoStore_pb2 as documentNoStore__pb2
import search_pb2 as search__pb2
import accounts_pb2 as accounts__pb2
import billing_pb2 as billing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='strongdoc.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.strongsalt.strongdoc.sdk.protoB\016StrongDocProto\210\001\001\222A\265\002\0227\n\rStrongDoc API\"!\n\nStrongSalt\032\023info@strongsalt.com2\0031.02\020application/json:\020application/jsonZ\212\001\n\207\001\n\nApiKeyAuth\022y\010\002\022dThe word \'Bearer\' and a space is required before the token.\nFor example,\nBearer authentication_token\032\rAuthorization \002rI\n\027More about gRPC-Gateway\022.https://github.com/grpc-ecosystem/grpc-gateway',
  serialized_pb=b'\n\x0fstrongdoc.proto\x12\x05proto\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\x0e\x64ocument.proto\x1a\x15\x64ocumentNoStore.proto\x1a\x0csearch.proto\x1a\x0e\x61\x63\x63ounts.proto\x1a\rbilling.proto\"\x15\n\x13GetConfigurationReq\"-\n\x14GetConfigurationResp\x12\x15\n\rconfiguration\x18\x01 \x01(\t2\xb9%\n\x10StrongDocService\x12\x84\x01\n\x14RegisterOrganization\x12\x1e.proto.RegisterOrganizationReq\x1a\x1f.proto.RegisterOrganizationResp\"+\x82\xd3\xe4\x93\x02%\" /v1/account/registerOrganization:\x01*\x12\x88\x01\n\x16ReactivateOrganization\x12\x1e.proto.RegisterOrganizationReq\x1a\x1f.proto.RegisterOrganizationResp\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/account/reactivateOrganization:\x01*\x12\x96\x01\n\x12RemoveOrganization\x12\x1c.proto.RemoveOrganizationReq\x1a\x1d.proto.RemoveOrganizationResp\"C\x82\xd3\xe4\x93\x02(*&/v1/account/removeOrganization/{force}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12y\n\x0cRegisterUser\x12\x16.proto.RegisterUserReq\x1a\x17.proto.RegisterUserResp\"8\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/account/registerUser:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12j\n\tListUsers\x12\x13.proto.ListUsersReq\x1a\x14.proto.ListUsersResp\"2\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/account/listUsers\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12q\n\nRemoveUser\x12\x14.proto.RemoveUserReq\x1a\x15.proto.RemoveUserResp\"6\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/account/removeUser:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12u\n\x0bPromoteUser\x12\x15.proto.PromoteUserReq\x1a\x16.proto.PromoteUserResp\"7\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/account/promoteUser:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12q\n\nDemoteUser\x12\x14.proto.DemoteUserReq\x1a\x15.proto.DemoteUserResp\"6\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/account/demoteUser:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12q\n\rListDocuments\x12\x17.proto.ListDocumentsReq\x1a\x18.proto.ListDocumentsResp\"-\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/doc/listDocs\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12z\n\x0eRemoveDocument\x12\x18.proto.RemoveDocumentReq\x1a\x19.proto.RemoveDocumentResp\"3\x82\xd3\xe4\x93\x02\x18*\x16/v1/doc/remove/{docID}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12Q\n\x14UploadDocumentStream\x12\x19.proto.UploadDocStreamReq\x1a\x1a.proto.UploadDocStreamResp\"\x00(\x01\x12k\n\x0eUploadDocument\x12\x13.proto.UploadDocReq\x1a\x14.proto.UploadDocResp\".\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/doc/upload:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12W\n\x16\x44ownloadDocumentStream\x12\x1b.proto.DownloadDocStreamReq\x1a\x1c.proto.DownloadDocStreamResp\"\x00\x30\x01\x12x\n\x10\x44ownloadDocument\x12\x15.proto.DownloadDocReq\x1a\x16.proto.DownloadDocResp\"5\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/doc/download/{docID}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12V\n\x15\x45ncryptDocumentStream\x12\x1a.proto.EncryptDocStreamReq\x1a\x1b.proto.EncryptDocStreamResp\"\x00(\x01\x30\x01\x12o\n\x0f\x45ncryptDocument\x12\x14.proto.EncryptDocReq\x1a\x15.proto.EncryptDocResp\"/\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/doc/encrypt:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12V\n\x15\x44\x65\x63ryptDocumentStream\x12\x1a.proto.DecryptDocStreamReq\x1a\x1b.proto.DecryptDocStreamResp\"\x00(\x01\x30\x01\x12t\n\x0f\x44\x65\x63ryptDocument\x12\x14.proto.DecryptDocReq\x1a\x15.proto.DecryptDocResp\"4\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/doc/decrypt/{docID}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12t\n\rShareDocument\x12\x17.proto.ShareDocumentReq\x1a\x18.proto.ShareDocumentResp\"0\x82\xd3\xe4\x93\x02\x15\"\x10/v1/doc/shareDoc:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12|\n\x0fUnshareDocument\x12\x19.proto.UnshareDocumentReq\x1a\x1a.proto.UnshareDocumentResp\"2\x82\xd3\xe4\x93\x02\x17\"\x12/v1/doc/unshareDoc:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x45\n\x05Login\x12\x0f.proto.LoginReq\x1a\x10.proto.LoginResp\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/auth/login:\x01*\x12V\n\x06Logout\x12\x10.proto.LogoutReq\x1a\x11.proto.LogoutResp\"\'\x82\xd3\xe4\x93\x02\x0c\"\n/v1/logout\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x62\n\x06Search\x12\x10.proto.SearchReq\x1a\x11.proto.SearchResp\"3\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/doc/search/{query}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x81\x01\n\x0e\x41\x64\x64SharableOrg\x12\x18.proto.AddSharableOrgReq\x1a\x19.proto.AddSharableOrgResp\":\x82\xd3\xe4\x93\x02\x1f\x32\x1a/v1/account/addSharableOrg:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x8d\x01\n\x11RemoveSharableOrg\x12\x1b.proto.RemoveSharableOrgReq\x1a\x1c.proto.RemoveSharableOrgResp\"=\x82\xd3\xe4\x93\x02\"2\x1d/v1/account/removeSharableOrg:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x99\x01\n\x14SetMultiLevelSharing\x12\x1e.proto.SetMultiLevelSharingReq\x1a\x1f.proto.SetMultiLevelSharingResp\"@\x82\xd3\xe4\x93\x02%\x1a /v1/account/setMultiLevelSharing:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x81\x01\n\x0eSetAccountInfo\x12\x18.proto.SetAccountInfoReq\x1a\x19.proto.SetAccountInfoResp\":\x82\xd3\xe4\x93\x02\x1f\x1a\x1a/v1/account/setAccountInfo:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x80\x01\n\x11GetBillingDetails\x12\x1b.proto.GetBillingDetailsReq\x1a\x1c.proto.GetBillingDetailsResp\"0\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/account/billing\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x9c\x01\n\x17GetBillingFrequencyList\x12!.proto.GetBillingFrequencyListReq\x1a\".proto.GetBillingFrequencyListResp\":\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/account/billing/frequency\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x9f\x01\n\x17SetNextBillingFrequency\x12!.proto.SetNextBillingFrequencyReq\x1a\".proto.SetNextBillingFrequencyResp\"=\x82\xd3\xe4\x93\x02\"\x1a\x1d/v1/account/billing/frequency:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x7f\n\x0fGetLargeTraffic\x12\x19.proto.GetLargeTrafficReq\x1a\x1a.proto.GetLargeTrafficResp\"5\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/account/largeTraffic\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12o\n\x0eGetAccountInfo\x12\x18.proto.GetAccountInfoReq\x1a\x19.proto.GetAccountInfoResp\"(\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/account\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12k\n\x0bGetUserInfo\x12\x15.proto.GetUserInfoReq\x1a\x16.proto.GetUserInfoResp\"-\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/account/user\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x91\x01\n\x12\x43hangeUserPassword\x12\x1c.proto.ChangeUserPasswordReq\x1a\x1d.proto.ChangeUserPasswordResp\">\x82\xd3\xe4\x93\x02#\x1a\x1e/v1/account/changeUserPassword:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12u\n\x0bSetUserInfo\x12\x15.proto.SetUserInfoReq\x1a\x16.proto.SetUserInfoResp\"7\x82\xd3\xe4\x93\x02\x1c\x1a\x17/v1/account/setUserInfo:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12x\n\x0fListCreditCards\x12\x19.proto.ListCreditCardsReq\x1a\x1a.proto.ListCreditCardsResp\".\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/billing/cards\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x86\x01\n\x10\x41\x64\x64PaymentMethod\x12\x1a.proto.AddPaymentMethodReq\x1a\x1b.proto.AddPaymentMethodResp\"9\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/billing/paymentMethod:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\xa3\x01\n\x17SetDefaultPaymentMethod\x12!.proto.SetDefaultPaymentMethodReq\x1a\".proto.SetDefaultPaymentMethodResp\"A\x82\xd3\xe4\x93\x02&\x1a!/v1/billing/paymentMethod/default:\x01*\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x12\x9a\x01\n\x13RemovePaymentMethod\x12\x1d.proto.RemovePaymentMethodReq\x1a\x1e.proto.RemovePaymentMethodResp\"D\x82\xd3\xe4\x93\x02)*\'/v1/billing/paymentMethod/remove/{pmID}\x92\x41\x12\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00\x42\xf0\x02\n\"com.strongsalt.strongdoc.sdk.protoB\x0eStrongDocProto\x88\x01\x01\x92\x41\xb5\x02\x12\x37\n\rStrongDoc API\"!\n\nStrongSalt\x1a\x13info@strongsalt.com2\x03\x31.02\x10\x61pplication/json:\x10\x61pplication/jsonZ\x8a\x01\n\x87\x01\n\nApiKeyAuth\x12y\x08\x02\x12\x64The word \'Bearer\' and a space is required before the token.\nFor example,\nBearer authentication_token\x1a\rAuthorization \x02rI\n\x17More about gRPC-Gateway\x12.https://github.com/grpc-ecosystem/grpc-gatewayb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,document__pb2.DESCRIPTOR,documentNoStore__pb2.DESCRIPTOR,search__pb2.DESCRIPTOR,accounts__pb2.DESCRIPTOR,billing__pb2.DESCRIPTOR,])




_GETCONFIGURATIONREQ = _descriptor.Descriptor(
  name='GetConfigurationReq',
  full_name='proto.GetConfigurationReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=207,
)


_GETCONFIGURATIONRESP = _descriptor.Descriptor(
  name='GetConfigurationResp',
  full_name='proto.GetConfigurationResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configuration', full_name='proto.GetConfigurationResp.configuration', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=254,
)

DESCRIPTOR.message_types_by_name['GetConfigurationReq'] = _GETCONFIGURATIONREQ
DESCRIPTOR.message_types_by_name['GetConfigurationResp'] = _GETCONFIGURATIONRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetConfigurationReq = _reflection.GeneratedProtocolMessageType('GetConfigurationReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGURATIONREQ,
  '__module__' : 'strongdoc_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetConfigurationReq)
  })
_sym_db.RegisterMessage(GetConfigurationReq)

GetConfigurationResp = _reflection.GeneratedProtocolMessageType('GetConfigurationResp', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGURATIONRESP,
  '__module__' : 'strongdoc_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetConfigurationResp)
  })
_sym_db.RegisterMessage(GetConfigurationResp)


DESCRIPTOR._options = None

_STRONGDOCSERVICE = _descriptor.ServiceDescriptor(
  name='StrongDocService',
  full_name='proto.StrongDocService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=257,
  serialized_end=5050,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterOrganization',
    full_name='proto.StrongDocService.RegisterOrganization',
    index=0,
    containing_service=None,
    input_type=accounts__pb2._REGISTERORGANIZATIONREQ,
    output_type=accounts__pb2._REGISTERORGANIZATIONRESP,
    serialized_options=b'\202\323\344\223\002%\" /v1/account/registerOrganization:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='ReactivateOrganization',
    full_name='proto.StrongDocService.ReactivateOrganization',
    index=1,
    containing_service=None,
    input_type=accounts__pb2._REGISTERORGANIZATIONREQ,
    output_type=accounts__pb2._REGISTERORGANIZATIONRESP,
    serialized_options=b'\202\323\344\223\002\'\"\"/v1/account/reactivateOrganization:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='RemoveOrganization',
    full_name='proto.StrongDocService.RemoveOrganization',
    index=2,
    containing_service=None,
    input_type=accounts__pb2._REMOVEORGANIZATIONREQ,
    output_type=accounts__pb2._REMOVEORGANIZATIONRESP,
    serialized_options=b'\202\323\344\223\002(*&/v1/account/removeOrganization/{force}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='RegisterUser',
    full_name='proto.StrongDocService.RegisterUser',
    index=3,
    containing_service=None,
    input_type=accounts__pb2._REGISTERUSERREQ,
    output_type=accounts__pb2._REGISTERUSERRESP,
    serialized_options=b'\202\323\344\223\002\035\"\030/v1/account/registerUser:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='ListUsers',
    full_name='proto.StrongDocService.ListUsers',
    index=4,
    containing_service=None,
    input_type=accounts__pb2._LISTUSERSREQ,
    output_type=accounts__pb2._LISTUSERSRESP,
    serialized_options=b'\202\323\344\223\002\027\022\025/v1/account/listUsers\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='RemoveUser',
    full_name='proto.StrongDocService.RemoveUser',
    index=5,
    containing_service=None,
    input_type=accounts__pb2._REMOVEUSERREQ,
    output_type=accounts__pb2._REMOVEUSERRESP,
    serialized_options=b'\202\323\344\223\002\033\"\026/v1/account/removeUser:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='PromoteUser',
    full_name='proto.StrongDocService.PromoteUser',
    index=6,
    containing_service=None,
    input_type=accounts__pb2._PROMOTEUSERREQ,
    output_type=accounts__pb2._PROMOTEUSERRESP,
    serialized_options=b'\202\323\344\223\002\034\"\027/v1/account/promoteUser:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='DemoteUser',
    full_name='proto.StrongDocService.DemoteUser',
    index=7,
    containing_service=None,
    input_type=accounts__pb2._DEMOTEUSERREQ,
    output_type=accounts__pb2._DEMOTEUSERRESP,
    serialized_options=b'\202\323\344\223\002\033\"\026/v1/account/demoteUser:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='ListDocuments',
    full_name='proto.StrongDocService.ListDocuments',
    index=8,
    containing_service=None,
    input_type=document__pb2._LISTDOCUMENTSREQ,
    output_type=document__pb2._LISTDOCUMENTSRESP,
    serialized_options=b'\202\323\344\223\002\022\022\020/v1/doc/listDocs\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='RemoveDocument',
    full_name='proto.StrongDocService.RemoveDocument',
    index=9,
    containing_service=None,
    input_type=document__pb2._REMOVEDOCUMENTREQ,
    output_type=document__pb2._REMOVEDOCUMENTRESP,
    serialized_options=b'\202\323\344\223\002\030*\026/v1/doc/remove/{docID}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='UploadDocumentStream',
    full_name='proto.StrongDocService.UploadDocumentStream',
    index=10,
    containing_service=None,
    input_type=document__pb2._UPLOADDOCSTREAMREQ,
    output_type=document__pb2._UPLOADDOCSTREAMRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadDocument',
    full_name='proto.StrongDocService.UploadDocument',
    index=11,
    containing_service=None,
    input_type=document__pb2._UPLOADDOCREQ,
    output_type=document__pb2._UPLOADDOCRESP,
    serialized_options=b'\202\323\344\223\002\023\"\016/v1/doc/upload:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='DownloadDocumentStream',
    full_name='proto.StrongDocService.DownloadDocumentStream',
    index=12,
    containing_service=None,
    input_type=document__pb2._DOWNLOADDOCSTREAMREQ,
    output_type=document__pb2._DOWNLOADDOCSTREAMRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadDocument',
    full_name='proto.StrongDocService.DownloadDocument',
    index=13,
    containing_service=None,
    input_type=document__pb2._DOWNLOADDOCREQ,
    output_type=document__pb2._DOWNLOADDOCRESP,
    serialized_options=b'\202\323\344\223\002\032\022\030/v1/doc/download/{docID}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='EncryptDocumentStream',
    full_name='proto.StrongDocService.EncryptDocumentStream',
    index=14,
    containing_service=None,
    input_type=documentNoStore__pb2._ENCRYPTDOCSTREAMREQ,
    output_type=documentNoStore__pb2._ENCRYPTDOCSTREAMRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EncryptDocument',
    full_name='proto.StrongDocService.EncryptDocument',
    index=15,
    containing_service=None,
    input_type=documentNoStore__pb2._ENCRYPTDOCREQ,
    output_type=documentNoStore__pb2._ENCRYPTDOCRESP,
    serialized_options=b'\202\323\344\223\002\024\"\017/v1/doc/encrypt:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='DecryptDocumentStream',
    full_name='proto.StrongDocService.DecryptDocumentStream',
    index=16,
    containing_service=None,
    input_type=documentNoStore__pb2._DECRYPTDOCSTREAMREQ,
    output_type=documentNoStore__pb2._DECRYPTDOCSTREAMRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DecryptDocument',
    full_name='proto.StrongDocService.DecryptDocument',
    index=17,
    containing_service=None,
    input_type=documentNoStore__pb2._DECRYPTDOCREQ,
    output_type=documentNoStore__pb2._DECRYPTDOCRESP,
    serialized_options=b'\202\323\344\223\002\031\022\027/v1/doc/decrypt/{docID}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='ShareDocument',
    full_name='proto.StrongDocService.ShareDocument',
    index=18,
    containing_service=None,
    input_type=document__pb2._SHAREDOCUMENTREQ,
    output_type=document__pb2._SHAREDOCUMENTRESP,
    serialized_options=b'\202\323\344\223\002\025\"\020/v1/doc/shareDoc:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='UnshareDocument',
    full_name='proto.StrongDocService.UnshareDocument',
    index=19,
    containing_service=None,
    input_type=document__pb2._UNSHAREDOCUMENTREQ,
    output_type=document__pb2._UNSHAREDOCUMENTRESP,
    serialized_options=b'\202\323\344\223\002\027\"\022/v1/doc/unshareDoc:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='proto.StrongDocService.Login',
    index=20,
    containing_service=None,
    input_type=accounts__pb2._LOGINREQ,
    output_type=accounts__pb2._LOGINRESP,
    serialized_options=b'\202\323\344\223\002\023\"\016/v1/auth/login:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='proto.StrongDocService.Logout',
    index=21,
    containing_service=None,
    input_type=accounts__pb2._LOGOUTREQ,
    output_type=accounts__pb2._LOGOUTRESP,
    serialized_options=b'\202\323\344\223\002\014\"\n/v1/logout\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='proto.StrongDocService.Search',
    index=22,
    containing_service=None,
    input_type=search__pb2._SEARCHREQ,
    output_type=search__pb2._SEARCHRESP,
    serialized_options=b'\202\323\344\223\002\030\022\026/v1/doc/search/{query}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='AddSharableOrg',
    full_name='proto.StrongDocService.AddSharableOrg',
    index=23,
    containing_service=None,
    input_type=accounts__pb2._ADDSHARABLEORGREQ,
    output_type=accounts__pb2._ADDSHARABLEORGRESP,
    serialized_options=b'\202\323\344\223\002\0372\032/v1/account/addSharableOrg:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='RemoveSharableOrg',
    full_name='proto.StrongDocService.RemoveSharableOrg',
    index=24,
    containing_service=None,
    input_type=accounts__pb2._REMOVESHARABLEORGREQ,
    output_type=accounts__pb2._REMOVESHARABLEORGRESP,
    serialized_options=b'\202\323\344\223\002\"2\035/v1/account/removeSharableOrg:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='SetMultiLevelSharing',
    full_name='proto.StrongDocService.SetMultiLevelSharing',
    index=25,
    containing_service=None,
    input_type=accounts__pb2._SETMULTILEVELSHARINGREQ,
    output_type=accounts__pb2._SETMULTILEVELSHARINGRESP,
    serialized_options=b'\202\323\344\223\002%\032 /v1/account/setMultiLevelSharing:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='SetAccountInfo',
    full_name='proto.StrongDocService.SetAccountInfo',
    index=26,
    containing_service=None,
    input_type=accounts__pb2._SETACCOUNTINFOREQ,
    output_type=accounts__pb2._SETACCOUNTINFORESP,
    serialized_options=b'\202\323\344\223\002\037\032\032/v1/account/setAccountInfo:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='GetBillingDetails',
    full_name='proto.StrongDocService.GetBillingDetails',
    index=27,
    containing_service=None,
    input_type=billing__pb2._GETBILLINGDETAILSREQ,
    output_type=billing__pb2._GETBILLINGDETAILSRESP,
    serialized_options=b'\202\323\344\223\002\025\022\023/v1/account/billing\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='GetBillingFrequencyList',
    full_name='proto.StrongDocService.GetBillingFrequencyList',
    index=28,
    containing_service=None,
    input_type=billing__pb2._GETBILLINGFREQUENCYLISTREQ,
    output_type=billing__pb2._GETBILLINGFREQUENCYLISTRESP,
    serialized_options=b'\202\323\344\223\002\037\022\035/v1/account/billing/frequency\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='SetNextBillingFrequency',
    full_name='proto.StrongDocService.SetNextBillingFrequency',
    index=29,
    containing_service=None,
    input_type=billing__pb2._SETNEXTBILLINGFREQUENCYREQ,
    output_type=billing__pb2._SETNEXTBILLINGFREQUENCYRESP,
    serialized_options=b'\202\323\344\223\002\"\032\035/v1/account/billing/frequency:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='GetLargeTraffic',
    full_name='proto.StrongDocService.GetLargeTraffic',
    index=30,
    containing_service=None,
    input_type=billing__pb2._GETLARGETRAFFICREQ,
    output_type=billing__pb2._GETLARGETRAFFICRESP,
    serialized_options=b'\202\323\344\223\002\032\022\030/v1/account/largeTraffic\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='GetAccountInfo',
    full_name='proto.StrongDocService.GetAccountInfo',
    index=31,
    containing_service=None,
    input_type=accounts__pb2._GETACCOUNTINFOREQ,
    output_type=accounts__pb2._GETACCOUNTINFORESP,
    serialized_options=b'\202\323\344\223\002\r\022\013/v1/account\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='GetUserInfo',
    full_name='proto.StrongDocService.GetUserInfo',
    index=32,
    containing_service=None,
    input_type=accounts__pb2._GETUSERINFOREQ,
    output_type=accounts__pb2._GETUSERINFORESP,
    serialized_options=b'\202\323\344\223\002\022\022\020/v1/account/user\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='ChangeUserPassword',
    full_name='proto.StrongDocService.ChangeUserPassword',
    index=33,
    containing_service=None,
    input_type=accounts__pb2._CHANGEUSERPASSWORDREQ,
    output_type=accounts__pb2._CHANGEUSERPASSWORDRESP,
    serialized_options=b'\202\323\344\223\002#\032\036/v1/account/changeUserPassword:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='SetUserInfo',
    full_name='proto.StrongDocService.SetUserInfo',
    index=34,
    containing_service=None,
    input_type=accounts__pb2._SETUSERINFOREQ,
    output_type=accounts__pb2._SETUSERINFORESP,
    serialized_options=b'\202\323\344\223\002\034\032\027/v1/account/setUserInfo:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='ListCreditCards',
    full_name='proto.StrongDocService.ListCreditCards',
    index=35,
    containing_service=None,
    input_type=billing__pb2._LISTCREDITCARDSREQ,
    output_type=billing__pb2._LISTCREDITCARDSRESP,
    serialized_options=b'\202\323\344\223\002\023\022\021/v1/billing/cards\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='AddPaymentMethod',
    full_name='proto.StrongDocService.AddPaymentMethod',
    index=36,
    containing_service=None,
    input_type=billing__pb2._ADDPAYMENTMETHODREQ,
    output_type=billing__pb2._ADDPAYMENTMETHODRESP,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/billing/paymentMethod:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='SetDefaultPaymentMethod',
    full_name='proto.StrongDocService.SetDefaultPaymentMethod',
    index=37,
    containing_service=None,
    input_type=billing__pb2._SETDEFAULTPAYMENTMETHODREQ,
    output_type=billing__pb2._SETDEFAULTPAYMENTMETHODRESP,
    serialized_options=b'\202\323\344\223\002&\032!/v1/billing/paymentMethod/default:\001*\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
  _descriptor.MethodDescriptor(
    name='RemovePaymentMethod',
    full_name='proto.StrongDocService.RemovePaymentMethod',
    index=38,
    containing_service=None,
    input_type=billing__pb2._REMOVEPAYMENTMETHODREQ,
    output_type=billing__pb2._REMOVEPAYMENTMETHODRESP,
    serialized_options=b'\202\323\344\223\002)*\'/v1/billing/paymentMethod/remove/{pmID}\222A\022b\020\n\016\n\nApiKeyAuth\022\000',
  ),
])
_sym_db.RegisterServiceDescriptor(_STRONGDOCSERVICE)

DESCRIPTOR.services_by_name['StrongDocService'] = _STRONGDOCSERVICE

# @@protoc_insertion_point(module_scope)
