def sravnenie(a):
    if a % 15 == 0:
        print("FizzBuzz")
    else:
        if a % 5 == 0:
            print("Fizz")
        else:
            if a % 3 == 0:
                print("Buzz")
            else:
                print(a)


for i in range(1, 101):
    sravnenie(i)
