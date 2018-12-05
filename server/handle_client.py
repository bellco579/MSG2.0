def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(1024).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    # client.send(bytes(prefix, "utf8")+msg)
    # broadcast(bytes(msg, "utf8"))
    # clients[client] = name

    while True:
        msg = client.recv(1024)
        print(msg)
        print(client)
        if msg != bytes("{quit}", "utf8"):
            self.client_socket.send(msg)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            # del clients[client]
            # broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


# def broadcast(msg, prefix=""):  # prefix is for name identification.
#     """Broadcasts a message to all the clients."""

#     for sock in clients:
#         sock.send(bytes(prefix, "utf8")+msg)
