students = {
    "Asha": [85, 90, 78],
    "Ravi": [70, 65, 88],
    "Meera": [92, 95, 89],
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(f"{name}: average mark = {average}")
