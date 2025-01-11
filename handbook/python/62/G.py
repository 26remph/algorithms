import pandas as pd


def need_to_work_better(df):
    return df[(df["maths"] == 2) | (df["physics"] == 2) | (df["computer science"] == 2)]


if __name__ == "__main__":
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = need_to_work_better(journal)
    print(journal)
    print(filtered)
