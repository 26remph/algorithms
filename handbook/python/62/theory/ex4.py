import pandas as pd


students_marks = {
    "student": ["Студент_1", "Студент_2", "Студент_3"],
    "math": [5, 3, 4],
    "physics": [4, 5, 6],
}
students = pd.DataFrame(students_marks)
print(students)

print(students.index)
print(students.columns)

students.index = ["A", "B", "C"]
print(students)

# access to attribute
print("\nAccess to attribute")
print(students.loc["B":])

# data type
print(type(students["student"]))
