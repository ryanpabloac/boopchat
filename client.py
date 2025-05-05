
import socket

class client():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def ip(self, ip):
        self.__ip = ip
    
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def address(self):
        return self.__address

    async def connect(self):
        server = (self.ip, self.port)
        try:
            self.__socket.connect(server)
            return(f"Connected at {self.ip}:{self.port}!")
        except socket.error as e: 
            return(f"Socket error: {str(e)}")

    async def close(self):
        self.__socket.close() 
        return("Connection terminated!")
    
    async def send(self, msg):
        self.__socket.sendall(msg.encode('utf-8'))
        return f"Mensagem: {msg}"

        # try:
        #     msg = "Ping"
        #     print(f"Mensagem: {msg}")
        #     s.sendall(msg.encode('utf-8'))

        #     amount_received = 0 
        #     amount_expected = len(msg) 
        #     while amount_received < amount_expected: 
        #         data = s.recv(16) 
        #         amount_received += len(data) 
        #         print ("Received: %s" % data) 
        # except socket.error as e: 
        #     print ("Socket error: %s" %str(e)) 
        # except Exception as e: 
        #     print ("Other exception: %s" %str(e)) 
        # finally: 
        #     print ("Closing connection to the server") 
        #     s.close() 
