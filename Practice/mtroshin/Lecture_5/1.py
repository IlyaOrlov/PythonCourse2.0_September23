# Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
# 1 найти наименьший элемент в массиве
# 2 поменять местами его и первый элемент в массиве
# 3 найти следующий наименьший элемент в массиве
# 4 и поменять местами его и второй элемент массива
# 5 продолжать это пока весь массив не будет отсортирован
# arr = [0,3,24,2,3,7]
#  здесь реализованный алгоритм
#  на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]

arr = [0, 3, 24, 2, 3, 7]

for i in range(len(arr)): #цикл проходит от 0 до последнего символа цикла
    minimal = i #индекс цифры в массиве
    for j in range(i+1, len(arr)): # проход по оставшимся цифрам в массиве (после текущего)
        if arr[j] < arr[minimal]:
            minimal = j
    if minimal != i:
        arr[i], arr[minimal] = arr[minimal], arr[i]

print(arr)