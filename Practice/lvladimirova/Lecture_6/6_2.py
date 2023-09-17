from random import randrange

def poisk(s):
    for i, x in enumerate(s):
        if s.index(x) != i:
            print(f"Первый повторяющийся элемент: {s[i]}")
            break
    else:
        print("Повторяющийся элемент не найден в списке!")


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 3, 2]
    print(arr)
    poisk(arr)
    # Для интереса попробовала создать рандомный список
    arr2 = [randrange(0,50) for i in range(5)]
    print(arr2)
    poisk(arr2)
