original_string = input("Введите строку: ")
string = original_string.lower()
new_string = string[::-1]
if new_string == string:
    print("True")
else:
    print("False")
