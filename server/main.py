from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from accept_incoming_connections import accept_incoming_connections

clients = {}
addresses = {}


HOST = '192.168.1.64'
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections,args = (SERVER,addresses))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()