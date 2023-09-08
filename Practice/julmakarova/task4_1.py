for i in range(1, 101):
    if not(i % 3):
        if not(i % 5):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif not(i % 5):
        print("Buzz")
    else:
        print(i)
