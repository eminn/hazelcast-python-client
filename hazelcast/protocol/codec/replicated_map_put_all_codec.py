from hazelcast.serialization.data import *
from hazelcast.serialization.bits import *
from hazelcast.protocol.client_message import ClientMessage
from hazelcast.protocol.custom_codec import *
from hazelcast.protocol.codec.replicated_map_message_type import *

REQUEST_TYPE = REPLICATEDMAP_PUTALL
RESPONSE_TYPE = 100
RETRYABLE = False


def calculate_size(name, entries):
    """ Calculates the request payload size"""
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += INT_SIZE_IN_BYTES
    for entries_item in entries:
        data_size += calculate_size_tuple<data, data >(entries_item)
    return data_size


def encode_request(name, entries):
    """ Encode request into client_message"""
    client_message = ClientMessage(payload_size=calculate_size(name, entries))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_int(len(entries))
    for entries_item in entries:
        client_message.append_tuple<data, data >(entries_item)
    client_message.update_frame_length()
    return client_message


def decode_response(client_message):
    """ Decode response from client message"""
    parameters = dict()
    return parameters



