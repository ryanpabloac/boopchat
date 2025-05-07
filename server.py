
import socket
ip = socket.gethostbyname(socket.gethostname())
address = (ip, 55555)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
print("Ligado", ip)

while True:
    client, add = server.accept()
    msg = client.recv(1024).decode("utf-8")
    if msg:
        print(f"{msg} recebida")
        client.close()
        
