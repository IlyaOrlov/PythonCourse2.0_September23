for i in range(1, 101, 15):
    print(i)
if i % 3:
    print("Fizz")
else:
    if i % 5:
        print("Buzz")
    else:
        if i % 15:
            print("FizzBuzz")
