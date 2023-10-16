def fun(a, b):
    return a / b


while True:
    x = input("Введите x: ")
    y = input("Введите y: ")
    try:
        res = fun(int(x), int(y))
        print(res)
    except ZeroDivisionError as ex:
        print(f"На ноль делить нельзя! Error: {ex}")
    except ValueError as ex:
        print(f"Надо указывать только числа! Error: {ex}")
    except Exception as ex:
        print(f"Exception: {ex}")
    else:
        break
    finally:
        print("Always!!!")

print("The end!")
