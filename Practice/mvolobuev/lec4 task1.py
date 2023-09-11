def sravnenie(a):
    d1 = a // 3 * 3
    d2 = a // 5 * 5
    d3 = a // 15 * 15
    if d3 == a: print("FizzBuzz")
    elif d1 == a: print("Fizz")
    elif d2 == a: print("Buzz")
    else:
        print(a)


n = 1
k = 101
for i in range(n , k):
    sravnenie(i)


