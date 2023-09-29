for x in range(1, 101):
    if x % 15 == 0:
        x = "FuzzBuzz"
    elif x % 5 == 0:
        x = "Buzz"
    elif x % 3 == 0:
        x = "Fuzz"
    print(x)
