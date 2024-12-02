import pandas as pd


students = pd.read_csv("sample_ds.csv")
print(students.head())

print(students.tail(3))

print(students[10:13])

# filtering data
print(students[students["test preparation course"] == "completed"]["math score"].head())

# best five result test from three discipline by asc
with_course = students[students["test preparation course"] == "completed"]
print(
    with_course[["math score", "reading score", "writing score"]]
    .sort_values(["math score", "reading score", "writing score"], ascending=False)
    .head()
)

# sorting by sum score
with_course = students[students["test preparation course"] == "completed"]
students["total score"] = (
    students["reading score"] + students["writing score"] + students["math score"]
)
print(students.sort_values(["total score"], ascending=False).head(6))
