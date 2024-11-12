import json
import time


NS = "NAME_CONTAINS"
PGT = "PRICE_GREATER_THAN"
PLT = "PRICE_LESS_THAN"
DA = "DATE_AFTER"
DB = "DATE_BEFORE"


def judge(record, sets):
    if_1 = sets[NS].lower() in record["name"].lower()
    if_2 = record["price"] >= int(sets[PGT])
    if_3 = record["price"] <= int(sets[PLT])

    date = time.strptime(record["date"], "%d.%m.%Y")
    _after = time.strptime(sets[DA], "%d.%m.%Y")
    _before = time.strptime(sets[DB], "%d.%m.%Y")
    if_4 = _after <= date <= _before

    is_pass = all([if_1, if_2, if_3, if_4])
    if is_pass:
        sets["count"] += 1

    return is_pass


def output(data: list, sets):
    data.sort(key=lambda x: (-judge(x, sets), x["id"]))
    count = sets["count"]

    return json.dumps(data[:count]) if count > 0 else json.dumps({})


def read_input():
    arr = json.loads(input())
    condition = {"count": 0}

    for _ in range(5):
        key, val = input().split()
        condition[key] = val

    return arr, condition


print(output(*read_input()))
