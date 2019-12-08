#coding:utf-8
import socket

host, port = ('', 8888)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("\n Server started on \n -port:" + str(port) + "\n")
 
while True:
    socket.listen(5)
    connection, address = socket.accept()
    print("/!\ A new guest has arrived on the port /!\ \n")
 
    data = connection.recv(1024)
    data = data.decode("utf8")
    print("data received from the guest: " + str(data))

connection.close()
socket.close()
