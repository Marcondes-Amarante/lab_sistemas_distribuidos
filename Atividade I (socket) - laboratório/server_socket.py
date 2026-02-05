import socket
from datetime import datetime

port = 8000
host_name = "127.0.0.1"

#criação e configuração do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_name, port))

#definição de quantas clintes ele pode escutar simultaneamente
server_socket.listen(1)

#tratamento do pedido recebido
while True:

    print("esperando conexão")

    client, connection = server_socket.accept()
    print("conexão estabelecida")
    
    mensg_op = "------ opções ------ \n 1 - horário \n 2 - inverter string"
    client.send(mensg_op.encode())


    while True:
        
        data_op = client.recv(1024).decode()

        if(data_op == "1"):
            horario = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            client.send(horario.encode())
            break
        elif(data_op == "2"):
            mensg_string = "digite a string"
            client.send(mensg_string.encode())

            data_string = client.recv(1024).decode()

            if isinstance(data_string, str):
                inverted_string = data_string[::-1]
                client.send(inverted_string.encode())
                break
            else:
                print("entrada inválida")
                break
        else:
            print("entrada inválida")
            break



