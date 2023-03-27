import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://reply:5555")

print("Sending request...")
socket.send(b"Hello")
message = socket.recv()
print("Received reply: %s" % message)
