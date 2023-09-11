for i in range(1, 101):
    if i % 15 == 0:
        i = "FuzzBuzz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 3 == 0:
        i = "Fuzz"
    print(i)
