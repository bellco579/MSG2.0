from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from client_processing import  Run_Client_Pocessing_Interface as Client_Processing
# import client_processing as cp


HOST = '192.168.1.64'
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    Client_Processing(SERVER)
    # ACCEPT_THREAD = Thread(target=accept_incoming_connections,args = (SERVER))
    # ACCEPT_THREAD.start()
    # ACCEPT_THREAD.join()
# SERVER.close()