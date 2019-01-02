#Exemplo do Livro
import socket

target_host = "www.google.com"
target_port = 80

#cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#faz o cliente se conectar
client.connect((target_host,target_port))

# envia alguns dados
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# recebe alguns dados
response = client.recv(4096)
print ("response")
