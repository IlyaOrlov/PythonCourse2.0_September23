def password(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return None


my_list = [2, 3, 4, 5, 3, 2]
result = password(my_list)
print(result)
