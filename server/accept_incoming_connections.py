from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from handle_client import handle_client

def accept_incoming_connections(SERVER,addresses):
    client, client_address = SERVER.accept()
    client.send(b'happy son of bytes')
    """Sets up handling for incoming clients."""
    while True:
        # print('client:',client, 'add:',client_address)
            # print('connected to: ',client_address)
            msg = client.recv(1024)
            print(msg)
            client.send(msg)
            # client.sendto(msg,client_address)

        # print("%s:%s has connected." % client_address)
        # client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        # addresses[client] = client_address
        # Thread(target=handle_client, args=(client,)).start()

