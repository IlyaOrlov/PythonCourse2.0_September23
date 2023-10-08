import random


p = input("Добрый день! О чём вы хотите поспорить? ")
a_list = ['Ты сам-то понял, что написал?', 'Аргументируй', 'И']
while not p == "хватит":
    print(random.choice(a_list))
    p = input("Я считаю это не так! Попробуй убедить меня: ")
else:
    print("Ну пока")
