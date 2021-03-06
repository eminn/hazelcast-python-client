from hazelcast.serialization.data import *
from hazelcast.serialization.bits import *
from hazelcast.protocol.client_message import ClientMessage
from hazelcast.protocol.custom_codec import *
from hazelcast.protocol.codec.executor_service_message_type import *

REQUEST_TYPE = EXECUTORSERVICE_SUBMITTOADDRESS
RESPONSE_TYPE = 105
RETRYABLE = False


def calculate_size(name, uuid, callable, address):
    """ Calculates the request payload size"""
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += calculate_size_str(uuid)
    data_size += calculate_size_data(callable)
    data_size += calculate_size_address(address)
    return data_size


def encode_request(name, uuid, callable, address):
    """ Encode request into client_message"""
    client_message = ClientMessage(payload_size=calculate_size(name, uuid, callable, address))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_str(uuid)
    client_message.append_data(callable)
    AddressCodec.encode(client_message, address)
    client_message.update_frame_length()
    return client_message


def decode_response(client_message):
    """ Decode response from client message"""
    parameters = dict(response=None)
    response=None
    if not client_message.read_bool():
        parameters['response'] = client_message.read_data()
    return parameters



