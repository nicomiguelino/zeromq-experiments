from time import sleep
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    print("Waiting for request...")
    message = socket.recv()
    socket.send(b"World")
