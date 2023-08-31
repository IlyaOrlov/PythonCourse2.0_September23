if __name__ == "__main__":

    start = float(input("Топлива  было  (л) ______ : "))
    end = float(input("Топлива осталось (л) ____ : "))
    distance = float(input("Пройденное расстояние (км): "))

    diff = start - end
    result = diff * 100 / distance
    print(f"\nРасход топлива {round(result, 1)}  литра на 100 км ")

    # вроде одна пробельная строчка допускается для разделения блоков по смыслу, логике и для красоты.