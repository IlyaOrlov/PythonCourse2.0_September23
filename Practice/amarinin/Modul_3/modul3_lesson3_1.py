if __name__ == "__main__":
    length = float(input("Введите длину  прямоугольника (м) : "))
    width = float(input("Введите ширину прямоугольника (м) : "))
    perimeter = round((length + width) * 2, 2)
    print(f"Периметр прямоугольника равен  {perimeter}  м.")
