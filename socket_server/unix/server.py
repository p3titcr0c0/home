#coding:utf-8
import socket

host, port = ('', 8888)

class color:
	GREEN = "\033[1;32m"
	RED = "\033[91m"
	CLOSE = "\033[37m"


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("\n" + color.GREEN + "Server started on \n -port:" + color.RED + str(port) + color.CLOSE + "\n")
 
while True:
    socket.listen(5)
    connection, address = socket.accept()
    print("/!\ A new guest has arrived on the port /!\ \n")
 
    data = connection.recv(1024)
    data = data.decode("utf8")
    print("data received from the guest: "+ color.RED + str(data) + color.CLOSE)

connection.close()
socket.close()
