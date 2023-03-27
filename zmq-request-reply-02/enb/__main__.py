import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def handle_message(socket, message):
    if message == b"RRC_CONNECTION_REQUEST":
        socket.send(b"RRC_CONNECTION_SETUP")
    elif message == b"RRC_CONNECTION_SETUP_COMPLETE":
        socket.send(b"RRC_CONNECTION_RECONFIGURATION")
    else:
        print(f"[ENB] Unknown message: {message}")
        socket.send(b"UNKNOWN")
        exit(0)

while True:
    message = socket.recv()
    print(f"[ENB] Received: {message}")

    handle_message(socket, message)
