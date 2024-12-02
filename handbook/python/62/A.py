import string

import pandas as pd


def length_stats(raw_text: str) -> pd.Series:
    exclude_list = set(string.punctuation + string.digits)
    raw_text = "".join([ch.lower() for ch in raw_text if ch not in exclude_list])

    ds = raw_text.split()
    ser = pd.Series(ds, index=ds).drop_duplicates()
    ser.sort_index(inplace=True)

    return ser.str.len()


if __name__ == "__main__":
    print("-- Answer --")
    print(length_stats("Мама мыла раму"))
    print(length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка."))
