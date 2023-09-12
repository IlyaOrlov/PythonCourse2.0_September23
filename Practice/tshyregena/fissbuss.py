start = 1
end = 100
while start < end:
    print(start)
    if start % 15 == 0:
        print(f"FizzBuzz")
    elif start % 5 == 0:
        print(f"Buzz")
    elif start % 3 == 0:
        print(f"Fizz")
    start += 1
