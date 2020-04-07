# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from strongdoc.proto.protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='billing.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.strongsalt.strongdoc.sdk.protoB\007Billing\210\001\001',
  serialized_pb=b'\n\rbilling.proto\x12\x05proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,protoc-gen-swagger/options/annotations.proto\">\n\x14GetBillingDetailsReq\x12&\n\x02\x61t\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x98\x06\n\x15GetBillingDetailsResp\x12/\n\x0bperiodStart\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tperiodEnd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\ttotalCost\x18\x03 \x01(\x01\x12\'\n\tdocuments\x18\x04 \x01(\x0b\x32\x14.proto.DocumentCosts\x12\"\n\x06search\x18\x05 \x01(\x0b\x32\x12.proto.SearchCosts\x12$\n\x07traffic\x18\x06 \x01(\x0b\x32\x13.proto.TrafficCosts\x12\x31\n\x10\x62illingFrequency\x18\x07 \x01(\x0b\x32\x17.proto.BillingFrequency:\xe5\x03\x92\x41\xe1\x03\n\x17*\x15GetBillingDetailsResp2\xc5\x03\x12\xc2\x03{\"periodStart\": \"2020-02-10T12:30:15.123Z\", \"periodEnd\": \"2020-03-01T00:00:00Z\", \"totalCost\": 800548.00, \"documents\": {\"cost\": 16.08, \"size\": 148193280, \"tier\": \"Document Storage Mid\"}, \"search\": {\"cost\": 2.00, \"size\": 58982400, \"tier\": \"Search Index Storage Low\"}, \"traffic\": {\"cost\": 0, \"incoming\": 500.456, \"outgoing\": 200.564, \"tier\": \"Network Traffic Free\"}, \"billingFrequency\": {\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}}\"\x1c\n\x1aGetBillingFrequencyListReq\"\xdb\x01\n\x1bGetBillingFrequencyListResp\x12\x35\n\x14\x62illingFrequencyList\x18\x01 \x03(\x0b\x32\x17.proto.BillingFrequency:\x84\x01\x92\x41\x80\x01\n\x1d*\x1bGetBillingFrequencyListResp2_\x12]{\"billingFrequencyList\": [{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}]}\"\xdb\x01\n\x1aSetNextBillingFrequencyReq\x12&\n\tfrequency\x18\x01 \x01(\x0e\x32\x13.proto.TimeInterval\x12-\n\tvalidFrom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:f\x92\x41\x63\n\x1c*\x1aSetNextBillingFrequencyReq2C\x12\x41{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}\"\xd8\x01\n\x1bSetNextBillingFrequencyResp\x12\x35\n\x14nextBillingFrequency\x18\x01 \x01(\x0b\x32\x17.proto.BillingFrequency:\x81\x01\x92\x41~\n\x1d*\x1bSetNextBillingFrequencyResp2]\x12[{\"nextBillingFrequency\": {\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}}\"<\n\x12GetLargeTrafficReq\x12&\n\x02\x61t\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd4\x04\n\x13GetLargeTrafficResp\x12*\n\x0clargeTraffic\x18\x01 \x03(\x0b\x32\x14.proto.TrafficDetail\x12/\n\x0bperiodStart\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tperiodEnd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\xb0\x03\x92\x41\xac\x03\n\x15*\x13GetLargeTrafficResp2\x92\x03\x12\x8f\x03{\"largeTraffic\": [{\"time\": \"2020-03-20T11:05:11.956889144Z\",\"userID\": \"user@company.com\",\"method\": \"GET\",\"URI\": \"/v1/account/billing\",\"incoming\": 810,\"outgoing\": 392},{\"time\":\"2020-03-20T11:30:34.630333618Z\",\"userID\": \"user2@company.com\",\"method\": \"GET\",\"URI\": \"/v1/account/largeTraffic\",\"incoming\": 816,\"outgoing\": 95}],\"periodStart\": \"2020-03-20T11:04:47.210Z\",\"periodEnd\": \"2020-04-01T00:00:00Z\"}\"\x8a\x01\n\rTrafficDetail\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06userID\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x0b\n\x03URI\x18\x04 \x01(\t\x12\x10\n\x08incoming\x18\x05 \x01(\x01\x12\x10\n\x08outgoing\x18\x06 \x01(\x01\"\x97\x02\n\x10\x42illingFrequency\x12&\n\tfrequency\x18\x01 \x01(\x0e\x32\x13.proto.TimeInterval\x12-\n\tvalidFrom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07validTo\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x7f\x92\x41|\n\x12*\x10\x42illingFrequency2f\x12\x64{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-03-01T00:00:15.123Z\", \"validTo\": \"2020-06-01T00:00:00Z\"}\"\x96\x01\n\rDocumentCosts\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x01\x12\x0c\n\x04size\x18\x02 \x01(\x01\x12\x0c\n\x04tier\x18\x03 \x01(\t:[\x92\x41X\n\x10*\x0e\x44ocumentsCosts2D\x12\x42{\"cost\": 16.08, \"size\": 148193280, \"tier\": \"Document Storage Mid\"}\"\x93\x01\n\x0bSearchCosts\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x01\x12\x0c\n\x04size\x18\x02 \x01(\x01\x12\x0c\n\x04tier\x18\x03 \x01(\t:Z\x92\x41W\n\r*\x0bSearchCosts2F\x12\x44{\"cost\": 2.00, \"size\": 58982400, \"tier\": \"Search Index Storage Low\"}\"\xbc\x01\n\x0cTrafficCosts\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x01\x12\x10\n\x08incoming\x18\x02 \x01(\x01\x12\x10\n\x08outgoing\x18\x03 \x01(\x01\x12\x0c\n\x04tier\x18\x04 \x01(\t:l\x92\x41i\n\x0e*\x0cTrafficCosts2W\x12U{\"cost\": 0, \"incoming\": 500.456, \"outgoing\": 200.564, \"tier\": \"Network Traffic Free\"}*6\n\x0cTimeInterval\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07MONTHLY\x10\x01\x12\n\n\x06YEARLY\x10\x02\x42\x30\n\"com.strongsalt.strongdoc.sdk.protoB\x07\x42illing\x88\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])

_TIMEINTERVAL = _descriptor.EnumDescriptor(
  name='TimeInterval',
  full_name='proto.TimeInterval',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTHLY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YEARLY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3233,
  serialized_end=3287,
)
_sym_db.RegisterEnumDescriptor(_TIMEINTERVAL)

TimeInterval = enum_type_wrapper.EnumTypeWrapper(_TIMEINTERVAL)
UNDEFINED = 0
MONTHLY = 1
YEARLY = 2



_GETBILLINGDETAILSREQ = _descriptor.Descriptor(
  name='GetBillingDetailsReq',
  full_name='proto.GetBillingDetailsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='at', full_name='proto.GetBillingDetailsReq.at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=103,
  serialized_end=165,
)


_GETBILLINGDETAILSRESP = _descriptor.Descriptor(
  name='GetBillingDetailsResp',
  full_name='proto.GetBillingDetailsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='periodStart', full_name='proto.GetBillingDetailsResp.periodStart', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='periodEnd', full_name='proto.GetBillingDetailsResp.periodEnd', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCost', full_name='proto.GetBillingDetailsResp.totalCost', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='documents', full_name='proto.GetBillingDetailsResp.documents', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search', full_name='proto.GetBillingDetailsResp.search', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic', full_name='proto.GetBillingDetailsResp.traffic', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billingFrequency', full_name='proto.GetBillingDetailsResp.billingFrequency', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A\341\003\n\027*\025GetBillingDetailsResp2\305\003\022\302\003{\"periodStart\": \"2020-02-10T12:30:15.123Z\", \"periodEnd\": \"2020-03-01T00:00:00Z\", \"totalCost\": 800548.00, \"documents\": {\"cost\": 16.08, \"size\": 148193280, \"tier\": \"Document Storage Mid\"}, \"search\": {\"cost\": 2.00, \"size\": 58982400, \"tier\": \"Search Index Storage Low\"}, \"traffic\": {\"cost\": 0, \"incoming\": 500.456, \"outgoing\": 200.564, \"tier\": \"Network Traffic Free\"}, \"billingFrequency\": {\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=960,
)


_GETBILLINGFREQUENCYLISTREQ = _descriptor.Descriptor(
  name='GetBillingFrequencyListReq',
  full_name='proto.GetBillingFrequencyListReq',
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
  serialized_start=962,
  serialized_end=990,
)


_GETBILLINGFREQUENCYLISTRESP = _descriptor.Descriptor(
  name='GetBillingFrequencyListResp',
  full_name='proto.GetBillingFrequencyListResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='billingFrequencyList', full_name='proto.GetBillingFrequencyListResp.billingFrequencyList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A\200\001\n\035*\033GetBillingFrequencyListResp2_\022]{\"billingFrequencyList\": [{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}]}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1212,
)


_SETNEXTBILLINGFREQUENCYREQ = _descriptor.Descriptor(
  name='SetNextBillingFrequencyReq',
  full_name='proto.SetNextBillingFrequencyReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='proto.SetNextBillingFrequencyReq.frequency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validFrom', full_name='proto.SetNextBillingFrequencyReq.validFrom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222Ac\n\034*\032SetNextBillingFrequencyReq2C\022A{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1215,
  serialized_end=1434,
)


_SETNEXTBILLINGFREQUENCYRESP = _descriptor.Descriptor(
  name='SetNextBillingFrequencyResp',
  full_name='proto.SetNextBillingFrequencyResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nextBillingFrequency', full_name='proto.SetNextBillingFrequencyResp.nextBillingFrequency', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A~\n\035*\033SetNextBillingFrequencyResp2]\022[{\"nextBillingFrequency\": {\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-02-10T12:30:15.123Z\"}}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1437,
  serialized_end=1653,
)


_GETLARGETRAFFICREQ = _descriptor.Descriptor(
  name='GetLargeTrafficReq',
  full_name='proto.GetLargeTrafficReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='at', full_name='proto.GetLargeTrafficReq.at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1655,
  serialized_end=1715,
)


_GETLARGETRAFFICRESP = _descriptor.Descriptor(
  name='GetLargeTrafficResp',
  full_name='proto.GetLargeTrafficResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='largeTraffic', full_name='proto.GetLargeTrafficResp.largeTraffic', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='periodStart', full_name='proto.GetLargeTrafficResp.periodStart', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='periodEnd', full_name='proto.GetLargeTrafficResp.periodEnd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A\254\003\n\025*\023GetLargeTrafficResp2\222\003\022\217\003{\"largeTraffic\": [{\"time\": \"2020-03-20T11:05:11.956889144Z\",\"userID\": \"user@company.com\",\"method\": \"GET\",\"URI\": \"/v1/account/billing\",\"incoming\": 810,\"outgoing\": 392},{\"time\":\"2020-03-20T11:30:34.630333618Z\",\"userID\": \"user2@company.com\",\"method\": \"GET\",\"URI\": \"/v1/account/largeTraffic\",\"incoming\": 816,\"outgoing\": 95}],\"periodStart\": \"2020-03-20T11:04:47.210Z\",\"periodEnd\": \"2020-04-01T00:00:00Z\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1718,
  serialized_end=2314,
)


_TRAFFICDETAIL = _descriptor.Descriptor(
  name='TrafficDetail',
  full_name='proto.TrafficDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='proto.TrafficDetail.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userID', full_name='proto.TrafficDetail.userID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='proto.TrafficDetail.method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='URI', full_name='proto.TrafficDetail.URI', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incoming', full_name='proto.TrafficDetail.incoming', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outgoing', full_name='proto.TrafficDetail.outgoing', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=2317,
  serialized_end=2455,
)


_BILLINGFREQUENCY = _descriptor.Descriptor(
  name='BillingFrequency',
  full_name='proto.BillingFrequency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='proto.BillingFrequency.frequency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validFrom', full_name='proto.BillingFrequency.validFrom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validTo', full_name='proto.BillingFrequency.validTo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222A|\n\022*\020BillingFrequency2f\022d{\"frequency\": \"MONTHLY\", \"validFrom\": \"2020-03-01T00:00:15.123Z\", \"validTo\": \"2020-06-01T00:00:00Z\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2458,
  serialized_end=2737,
)


_DOCUMENTCOSTS = _descriptor.Descriptor(
  name='DocumentCosts',
  full_name='proto.DocumentCosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='proto.DocumentCosts.cost', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='proto.DocumentCosts.size', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tier', full_name='proto.DocumentCosts.tier', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\222AX\n\020*\016DocumentsCosts2D\022B{\"cost\": 16.08, \"size\": 148193280, \"tier\": \"Document Storage Mid\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2740,
  serialized_end=2890,
)


_SEARCHCOSTS = _descriptor.Descriptor(
  name='SearchCosts',
  full_name='proto.SearchCosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='proto.SearchCosts.cost', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='proto.SearchCosts.size', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tier', full_name='proto.SearchCosts.tier', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\222AW\n\r*\013SearchCosts2F\022D{\"cost\": 2.00, \"size\": 58982400, \"tier\": \"Search Index Storage Low\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2893,
  serialized_end=3040,
)


_TRAFFICCOSTS = _descriptor.Descriptor(
  name='TrafficCosts',
  full_name='proto.TrafficCosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='proto.TrafficCosts.cost', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incoming', full_name='proto.TrafficCosts.incoming', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outgoing', full_name='proto.TrafficCosts.outgoing', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tier', full_name='proto.TrafficCosts.tier', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\222Ai\n\016*\014TrafficCosts2W\022U{\"cost\": 0, \"incoming\": 500.456, \"outgoing\": 200.564, \"tier\": \"Network Traffic Free\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3043,
  serialized_end=3231,
)

_GETBILLINGDETAILSREQ.fields_by_name['at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBILLINGDETAILSRESP.fields_by_name['periodStart'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBILLINGDETAILSRESP.fields_by_name['periodEnd'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBILLINGDETAILSRESP.fields_by_name['documents'].message_type = _DOCUMENTCOSTS
_GETBILLINGDETAILSRESP.fields_by_name['search'].message_type = _SEARCHCOSTS
_GETBILLINGDETAILSRESP.fields_by_name['traffic'].message_type = _TRAFFICCOSTS
_GETBILLINGDETAILSRESP.fields_by_name['billingFrequency'].message_type = _BILLINGFREQUENCY
_GETBILLINGFREQUENCYLISTRESP.fields_by_name['billingFrequencyList'].message_type = _BILLINGFREQUENCY
_SETNEXTBILLINGFREQUENCYREQ.fields_by_name['frequency'].enum_type = _TIMEINTERVAL
_SETNEXTBILLINGFREQUENCYREQ.fields_by_name['validFrom'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SETNEXTBILLINGFREQUENCYRESP.fields_by_name['nextBillingFrequency'].message_type = _BILLINGFREQUENCY
_GETLARGETRAFFICREQ.fields_by_name['at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETLARGETRAFFICRESP.fields_by_name['largeTraffic'].message_type = _TRAFFICDETAIL
_GETLARGETRAFFICRESP.fields_by_name['periodStart'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETLARGETRAFFICRESP.fields_by_name['periodEnd'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRAFFICDETAIL.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BILLINGFREQUENCY.fields_by_name['frequency'].enum_type = _TIMEINTERVAL
_BILLINGFREQUENCY.fields_by_name['validFrom'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BILLINGFREQUENCY.fields_by_name['validTo'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['GetBillingDetailsReq'] = _GETBILLINGDETAILSREQ
DESCRIPTOR.message_types_by_name['GetBillingDetailsResp'] = _GETBILLINGDETAILSRESP
DESCRIPTOR.message_types_by_name['GetBillingFrequencyListReq'] = _GETBILLINGFREQUENCYLISTREQ
DESCRIPTOR.message_types_by_name['GetBillingFrequencyListResp'] = _GETBILLINGFREQUENCYLISTRESP
DESCRIPTOR.message_types_by_name['SetNextBillingFrequencyReq'] = _SETNEXTBILLINGFREQUENCYREQ
DESCRIPTOR.message_types_by_name['SetNextBillingFrequencyResp'] = _SETNEXTBILLINGFREQUENCYRESP
DESCRIPTOR.message_types_by_name['GetLargeTrafficReq'] = _GETLARGETRAFFICREQ
DESCRIPTOR.message_types_by_name['GetLargeTrafficResp'] = _GETLARGETRAFFICRESP
DESCRIPTOR.message_types_by_name['TrafficDetail'] = _TRAFFICDETAIL
DESCRIPTOR.message_types_by_name['BillingFrequency'] = _BILLINGFREQUENCY
DESCRIPTOR.message_types_by_name['DocumentCosts'] = _DOCUMENTCOSTS
DESCRIPTOR.message_types_by_name['SearchCosts'] = _SEARCHCOSTS
DESCRIPTOR.message_types_by_name['TrafficCosts'] = _TRAFFICCOSTS
DESCRIPTOR.enum_types_by_name['TimeInterval'] = _TIMEINTERVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBillingDetailsReq = _reflection.GeneratedProtocolMessageType('GetBillingDetailsReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGDETAILSREQ,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBillingDetailsReq)
  })
_sym_db.RegisterMessage(GetBillingDetailsReq)

GetBillingDetailsResp = _reflection.GeneratedProtocolMessageType('GetBillingDetailsResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGDETAILSRESP,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBillingDetailsResp)
  })
_sym_db.RegisterMessage(GetBillingDetailsResp)

GetBillingFrequencyListReq = _reflection.GeneratedProtocolMessageType('GetBillingFrequencyListReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGFREQUENCYLISTREQ,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBillingFrequencyListReq)
  })
_sym_db.RegisterMessage(GetBillingFrequencyListReq)

GetBillingFrequencyListResp = _reflection.GeneratedProtocolMessageType('GetBillingFrequencyListResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGFREQUENCYLISTRESP,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBillingFrequencyListResp)
  })
_sym_db.RegisterMessage(GetBillingFrequencyListResp)

SetNextBillingFrequencyReq = _reflection.GeneratedProtocolMessageType('SetNextBillingFrequencyReq', (_message.Message,), {
  'DESCRIPTOR' : _SETNEXTBILLINGFREQUENCYREQ,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.SetNextBillingFrequencyReq)
  })
_sym_db.RegisterMessage(SetNextBillingFrequencyReq)

SetNextBillingFrequencyResp = _reflection.GeneratedProtocolMessageType('SetNextBillingFrequencyResp', (_message.Message,), {
  'DESCRIPTOR' : _SETNEXTBILLINGFREQUENCYRESP,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.SetNextBillingFrequencyResp)
  })
_sym_db.RegisterMessage(SetNextBillingFrequencyResp)

GetLargeTrafficReq = _reflection.GeneratedProtocolMessageType('GetLargeTrafficReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLARGETRAFFICREQ,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetLargeTrafficReq)
  })
_sym_db.RegisterMessage(GetLargeTrafficReq)

GetLargeTrafficResp = _reflection.GeneratedProtocolMessageType('GetLargeTrafficResp', (_message.Message,), {
  'DESCRIPTOR' : _GETLARGETRAFFICRESP,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetLargeTrafficResp)
  })
_sym_db.RegisterMessage(GetLargeTrafficResp)

TrafficDetail = _reflection.GeneratedProtocolMessageType('TrafficDetail', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICDETAIL,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.TrafficDetail)
  })
_sym_db.RegisterMessage(TrafficDetail)

BillingFrequency = _reflection.GeneratedProtocolMessageType('BillingFrequency', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGFREQUENCY,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.BillingFrequency)
  })
_sym_db.RegisterMessage(BillingFrequency)

DocumentCosts = _reflection.GeneratedProtocolMessageType('DocumentCosts', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTCOSTS,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.DocumentCosts)
  })
_sym_db.RegisterMessage(DocumentCosts)

SearchCosts = _reflection.GeneratedProtocolMessageType('SearchCosts', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCOSTS,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.SearchCosts)
  })
_sym_db.RegisterMessage(SearchCosts)

TrafficCosts = _reflection.GeneratedProtocolMessageType('TrafficCosts', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICCOSTS,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:proto.TrafficCosts)
  })
_sym_db.RegisterMessage(TrafficCosts)


DESCRIPTOR._options = None
_GETBILLINGDETAILSRESP._options = None
_GETBILLINGFREQUENCYLISTRESP._options = None
_SETNEXTBILLINGFREQUENCYREQ._options = None
_SETNEXTBILLINGFREQUENCYRESP._options = None
_GETLARGETRAFFICRESP._options = None
_BILLINGFREQUENCY._options = None
_DOCUMENTCOSTS._options = None
_SEARCHCOSTS._options = None
_TRAFFICCOSTS._options = None
# @@protoc_insertion_point(module_scope)
