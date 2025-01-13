from collections.abc import Hashable

import numpy as np
import pandas as pd


def values(func, start, end, step) -> pd.Series:
    ds = pd.Series(
        np.arange(start, end + step, step), index=np.arange(start, end + step, step)
    )
    return ds.apply(func)


def min_extremum(ds: pd.Series) -> Hashable:
    return ds.idxmin()


def max_extremum(ds: pd.Series) -> Hashable:
    return ds.idxmax()


if __name__ == "__main__":
    data = values(lambda x: x**2 + 2 * x + 1, -1.5, 1.7, 0.1)
    print(data)
    print(min_extremum(data))
    print(max_extremum(data))
