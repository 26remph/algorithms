from string import digits, punctuation

import pandas as pd


def length_stats(raw_text: str) -> tuple[pd.Series, pd.Series]:
    exclude = set(punctuation + digits)
    ds = "".join([ch.lower() for ch in raw_text if ch not in exclude]).split()
    ser = pd.Series(ds, index=ds).drop_duplicates().sort_index().str.len()
    return ser[ser % 2 > 0], ser[ser % 2 == 0]


if __name__ == "__main__":
    odd, even = length_stats("Мама мыла раму")
    print(odd)
    print(even)

    odd, even = length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка.")
    print(odd)
    print(even)
