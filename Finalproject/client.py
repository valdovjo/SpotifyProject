import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to shared server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1, 2):
    print(f"Sending request …")
    socket.send_string("Picking a random song from Spotify API")

    #  Get the reply.
    message = socket.recv(1024)
    mes = message.decode("utf-8")
    print(f"Received reply: {mes}")

