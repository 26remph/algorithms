import pandas as pd


def cheque(price: pd.Series, **kwargs) -> pd.DataFrame:
    cart = pd.Series(kwargs, name="number", dtype=int).groupby(level=0).sum()

    df = pd.DataFrame(price.index, columns=["product"])
    df["price"] = price.values
    df = (
        df.join(cart, how="inner", on="product")
        .assign(cost=lambda x: x["price"] * x["number"])
        .sort_values(by="product")
    )
    df.index = range(df.shape[0])
    return df


def discount(income: pd.DataFrame):
    new_cheque = income.copy()
    new_cheque["cost"] = new_cheque.apply(
        lambda row: row["cost"] * 0.5 if row["number"] > 2 else row["cost"], axis=1
    )
    return new_cheque


if __name__ == "__main__":
    products = ["bread", "milk", "soda", "cream"]
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    with_discount = discount(result)
    print(result)
    print(with_discount)
