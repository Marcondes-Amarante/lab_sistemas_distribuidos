import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class services(rpyc.Service):

    def exposed_time(self):
        horario = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        return horario
    
    def exposed_inverter_string(self, string):
        if isinstance(string, str):
            string_invertida = string[::-1]
            return string_invertida
        else:
            print("entrada inválida")

server = ThreadedServer(
    services,
    hostname="127.0.0.1",
    port=8000
)

if __name__ == "__main__":
    server.start()

