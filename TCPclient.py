import socket

#create socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #Take an IPV4 address.  #TCP oriented socket
ip = socket.gethostbyname("www.google.com")
print(ip)
port = 80
address = (ip,port)

client.connect(address)

data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
sent_data = client.send(data.encode('utf-8'))
print(sent_data)

recieved_data = client.recv(200000).decode('utf-8')
print(recieved_data)
