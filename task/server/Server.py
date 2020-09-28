import socket
import threading
class Mythread(threading.Thread):
    def __init__(self,client):
            threading.Thread.__init__(self)
            self.client=client
    def run(self):
        word = self.client.recv(1000)
        word = word.decode("utf-8")
        word ='Hello'+word
        word = bytes(word, "utf-8")
        self.client.send(word)
        
    

s1 = socket.socket()


hostname = "127.0.0.1"
port = 5656

s1.bind((hostname, port))
s1.listen(1)

while True:
        client,addr = s1.accept()
        t1=Mythread(client)
        t1.start()

       



