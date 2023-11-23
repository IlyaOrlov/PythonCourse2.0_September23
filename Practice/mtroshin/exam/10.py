# 10. Пользователь вводит с клавиатуры числа. Необходимо подобрать оптимальную структуру данных для их хранения и написать алгоритм,
# удаляющий из этой структуры данных числа, НЕ кратные 10 (обойтись без создания новой структуры данных).

# список
nums = []

while True:
    if (num := input("Введите число (пустую строку - для завершения): ")) == '':
        break # переход к алгоритму удаления чисел не кратных 10
    else:
        # добавление новых чисел в цикле
        nums.append(int(num))
        print(f"Текущее множество чисел:{nums}")

# алгоритм удаления чисел не четных 10 (при остановке добавления)
k = 0 # коэффициент уменьшения индекса при уменьшении длины списка от удаления элементов
for i in range(len(nums)):
    if nums[i-k] % 10 != 0:
        nums.remove(nums[i-k])
        k += 1

print(f"Множество чисел после удаления кратных 10:{nums}")
