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


if __name__ == "__main__":
    # test example 1
    products = ["bread", "milk", "soda", "cream"]
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    print(result)

    # test example 2
    products = ["toy_bear", "toy_doll", "toy_elephant", "toy_car", "any_toy"]
    prices = [100, 200, 240, 300, 500]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, toy_elephant=1, toy_bear=2, toy_doll=4)
    print(result)
