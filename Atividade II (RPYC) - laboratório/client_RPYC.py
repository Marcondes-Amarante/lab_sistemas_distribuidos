import rpyc

host_name = "127.0.0.1"
port = 8000

mensg_op = "------ opções ------ \n 1 - horário \n 2 - inverter string"
print(mensg_op)
op = input("escolha uma opção: ")

connection = rpyc.connect(host_name, port)

if(op == "1"):
    horario = connection.root.time()
    print(horario)
elif(op == "2"):
    string = input("digite a string: ")
    string_invertida = connection.root.inverter_string(string)
    print(string_invertida)