#coding:utf-8
import socket
 
host, port = ('localhost', 8888)
 
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("are you (guest) connected")
    data = input("Send the data: ")
    data = data.encode("utf8")
    socket.sendall(data)
    
except:
    print("Err: impossible connection")
finally:
    socket.close()
