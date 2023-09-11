if __name__ == "__main__":
    start = 1
    end = 100
    for i in range(start, end + 1):
        if i % 15 == 0:
            i = 'FizzBuzz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 3 == 0:
            i = 'Fizz'
        print(i)
