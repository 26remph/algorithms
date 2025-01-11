import pandas as pd


def best(df: pd.DataFrame) -> pd.DataFrame:
    # cond = df['maths'] > 3 | df['physics'] > 3 | df['computer science'] > 3
    return df[(df["maths"] > 3) & (df["physics"] > 3) & (df["computer science"] > 3)]


if __name__ == "__main__":
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)
