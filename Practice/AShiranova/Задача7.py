english_speakers = {"Илья Орлов", "Андрей Ширанов", "Иван Иванов", "Сергей Сергеев", "Александр Миронов"}
python_programmers = ["Илья Орлов", "Сергей Сергеев", "Максимилиан Грачев", "Степан Степанов"]

python_only_employees = []

for employee in python_programmers:
    if employee not in english_speakers:
        python_only_employees.append(employee)

print("Сотрудники, которые знают Python, но не знают Английский :")
for employee in python_only_employees:
    print(employee)

#Для решения данной задачи можно использовать две структуры данных:
#множество для хранения сотрудников, владеющих английским языком, и список для хранения сотрудников, знающих Python.