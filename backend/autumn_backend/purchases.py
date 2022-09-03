import json
import time


def judge(record, sets):

    if_1 = sets['NAME_CONTAINS'].lower() in record['name'].lower()
    if_2 = record['price'] >= int(sets['PRICE_GREATER_THAN'])
    if_3 = record['price'] <= int(sets['PRICE_LESS_THAN'])

    date = time.strptime(record['date'], '%d.%m.%Y')
    _after = time.strptime(sets['DATE_AFTER'], '%d.%m.%Y')
    _before = time.strptime(sets['DATE_BEFORE'], '%d.%m.%Y')
    if_4 = _after <= date <= _before

    is_true = all([if_1, if_2, if_3, if_4])
    if is_true:
        sets['match'] += 1

    return is_true


def output(data: list, sets):

    data.sort(key=lambda x: (-judge(x, sets), x['id']))
    count = sets['match']

    return json.dumps(data[:count]) if count > 0 else json.dumps({})


def read_input():
    arr = json.loads(input())
    condition = {'match': 0}

    for _ in range(5):
        key, val = input().split()
        condition[key] = val

    return arr, condition


print(output(*read_input()))
