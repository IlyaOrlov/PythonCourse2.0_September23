start = 1
end = 100
while start < end:
    print(start)
    if start % 3 == 0:
        print(f"Fizz")
    elif start % 5 == 0:
        print(f"Buzz")
    if start % 15 == 0:  # Не поняла почему, если ставить ещё раз elif, не работает
        print(f"FizzBuzz")
    start += 1
