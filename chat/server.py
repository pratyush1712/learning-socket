from http.server import ThreadingHTTPServer
import socket
import threading

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64 # maximum number of bytes a message from a client can be of
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# anything that hits this address will be linked to the above socket
server.bind(ADDR)


def handleClient(conn, addr):
    """
    A function to handle a single connection between a particular client and the entire server
    """
    print("a new connection found: ", addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # the next message
            print(f"[{addr}]: {msg}")
            if msg == "disconnect.":
                connected = False
            conn.send("Msg Received".encode(FORMAT))
    conn.close()

def start():
    server.listen() # start listening to connections
    print(f"[LISTENING] Serving is listening on {SERVER}/{PORT}...")
    while True:
        conn, addr = server.accept() # accept new connection
        thread = threading.Thread(target=handleClient, args=(conn, addr)) # start a thread that handles connection between server and client
        thread.start()
        print("Active threads/active clients = ", threading.activeCount() -1) # -1 because one thread is always running

print("[STARTING] Serving is starting...")
start()