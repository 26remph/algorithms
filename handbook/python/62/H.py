
import pandas as pd


def update(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(
        average=round((df["maths"] + df["physics"] + df["computer science"]) / 3, 6)
    )
    df.sort_values(by=["average", "name"], ascending=[False, True], inplace=True)
    return df


if __name__ == "__main__":
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)
