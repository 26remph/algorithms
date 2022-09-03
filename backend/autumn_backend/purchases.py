import json
import time


def judge(record, _filter):

    if_1 = _filter['NAME_CONTAINS'].lower() in record['name'].lower()
    if_2 = record['price'] >= int(_filter['PRICE_GREATER_THAN'])
    if_3 = record['price'] <= int(_filter['PRICE_LESS_THAN'])

    date = time.strptime(record['date'], '%d.%m.%Y')
    _after = time.strptime(_filter['DATE_AFTER'], '%d.%m.%Y')
    _before = time.strptime(_filter['DATE_BEFORE'], '%d.%m.%Y')
    if_4 = _after <= date <= _before

    is_true = all([if_1, if_2, if_3, if_4])
    if is_true:
        _filter['match'] += 1

    return is_true


def output(data: list, _filter):

    data.sort(key=lambda x: (-judge(x, _filter), x['id']))
    count = _filter['match']

    return json.dumps(data[:count]) if count > 0 else json.dumps({})


def read_input():
    arr = json.loads(input())
    condition = {'match': 0}

    for _ in range(5):
        key, val = input().split()
        condition[key] = val

    return arr, condition


print(output(*read_input()))
