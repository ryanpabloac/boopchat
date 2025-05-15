# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = '15.228.79.169'  # Public IP
# port = 12345
# try:
#     s.connect((host, port))
#     print(s.recv(1024).decode())
#     s.close()
# except Exception as e:
#     print(f"Connection failed: {e}")

# import socket
# import streamlit as st

# st.title("Servidor")
# data_payload = 4096
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip = "172.31.39.218"
# port = 55556
# server_address=(ip, port)
# st.write(f"Server ON {ip}:{port}")
# sock.bind(server_address)

# sock.listen(5)

# st.write("### Mensagem")
# while True:
#     client, address = sock.accept
#     data = client.recv(data_payload)
#     if data:
#         st.write(f"{address}: {data}")
#         client.send(data)
#         client.close()

# def server(host = 'localhost', port=8080):
#     data_payload = 2048 #The maximum amount of data to be received at once
#     # Create a TCP socket
#     sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
#     # Enable reuse address/port 
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     # Bind the socket to the port
#     server_address = (host, port)
#     print ("Starting up echo server  on %s port %s" % server_address)
#     sock.bind(server_address)
#     # Listen to clients, argument specifies the max no. of queued connections
#     sock.listen(5) 
#     i = 0
#     while True: 
#         print ("Client connected")
#         client, address = sock.accept() 
#         data = client.recv(data_payload) 
#         if data:
#             print ("Mensagem enviada: %s" %data)
            
#             print ("Mensagem %s enviada pra to %s" % (data, address))
#             # end connection
#             client.close()       
# server()
