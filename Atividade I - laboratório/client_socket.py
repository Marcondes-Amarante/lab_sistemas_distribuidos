import socket

host_name = "127.0.0.1"
port = 8000

#inicializando socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    while True:
        client_socket.connect((host_name, port))
        print("conexão bem sucedida")

        menu = client_socket.recv(1024).decode()
        print(menu)

        op = input()
        client_socket.send(op.encode())

        if(op == "1"):
            data = client_socket.recv(1024).decode()
            print(data)
            break
        elif(op == "2"):
            string_request = client_socket.recv(1024).decode()
            print(string_request)

            string = input()
            client_socket.send(string.encode())

            inverted_string = client_socket.recv(1024).decode()
            print(inverted_string)

            break
        else:
            print("opção inválida")
            break
except:
    print("falha em se conctar ao servidor")

