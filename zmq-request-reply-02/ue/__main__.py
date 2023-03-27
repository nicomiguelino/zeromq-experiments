from time import sleep
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://zmq-enb:5555")

tx_messages = [
    b"RRC_CONNECTION_REQUEST",
    b"RRC_CONNECTION_SETUP_COMPLETE",
    b"RETURN_OF_THE_KING",
]

for message in tx_messages:
    print(f"[UE] Sending: {message}")
    socket.send(message)

    sleep(2)

    message = socket.recv()
    print(f"[UE] Received: {message}")
