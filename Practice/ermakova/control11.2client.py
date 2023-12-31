import socket
import pickle
# import time
import User


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        # Здесь такое маленькое время ожидания роли не играет,
        # даже если одновременно запустить более 5 клиентов, вводить все равно будем по одному,
        # значит в очереди будет оставаться меньше 5.
        # Если поставить время ожидания больше и быстрее вводить клиентов,
        # в очереди могут оказаться больше 5 клиентов одновременно,
        # и сервер вернет ошибку ConnectionRefusedError: [WinError 10061]
        # Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение.
        # time.sleep(5)
        self._socket.send(pickle.dumps(user))
        print("Данные отправлены!")


if __name__ == '__main__':
    while True:
        name = input("Введите имя пользователя или стоп, "
                     "если хотите остановиться(или ничего не вводите): ")
        if name == "стоп" or len(name) == 0:
            break
        age = input("Введите возраст пользователя или стоп, "
                    "если хотите остановиться(или ничего не вводите) : ")
        if age == "стоп" or len(age) == 0:
            break
        user = User.User(name, age)
        myclient = TcpClient(host='127.0.0.1', port=5555)
        myclient.run()
