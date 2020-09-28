import socket
import xml.sax
from myparser import Handler

c1 = socket.socket()

hostname = "127.0.0.1"
port = 5656

c1.connect((hostname,port))
print("Please enter your word")
name = input()
name = bytes(name, "utf-8")
c1.send(name)

result = c1.recv(1000)
result = result.decode("utf-8")

xml.sax.parseString(result,Handler())
#print(result)
