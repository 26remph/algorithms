from typing import List, Tuple, Optional, Dict, Union
import time
import json
import time


# COUNTER: int = 0

def judge(element, _filter):

    print(element)
    f1 = _filter['NAME_CONTAINS'] in element['name']
    f2 = element['price'] >= int(_filter['PRICE_GREATER_THAN'])
    f3 = element['price'] <= int(_filter['PRICE_LESS_THAN'])
    date = time.strptime(element['date'], '%d.%m.%Y')
    date_after = time.strptime(_filter['DATE_AFTER'], '%d.%m.%Y')
    date_before = time.strptime(_filter['DATE_BEFORE'], '%d.%m.%Y')
    print(date, date_after, date_before)
    f4 = date_after <= date <= date_before

    print(f1, f2, f3, f4)
    print(_filter['NAME_CONTAINS'])
    is_judge = all([f1, f2, f3, f4])
    if is_judge:
        # global COUNTER
        # COUNTER += 1
        _filter['match'] += 1

    print(_filter['match'])
    return is_judge


def foo(input_dict, _filter) -> str:
    output_dict: list = []

    print(_filter)

    # for x in input_dict:
    #     print(x)
    #     print(x['price'], type(x['price']))

    output_dict = sorted(input_dict, key=lambda x: (-judge(x, _filter), x['id']))
    print('-' * 50)

    count = _filter['match']
    return json.dumps(output_dict[:count])


def read_input() -> Tuple[dict, Dict[str, Union[str, int]]]:

    # input_dict = json.loads(input())
    with open('input_report.json') as f:
        input_dict = json.load(f)

    _filter: Dict[str, Union[str, int]] = {'match': 0}
    for _ in range(5):
        key, val = input().split()
        _filter[key] = val

    return input_dict, _filter


if __name__ == '__main__':
    data, _filter = read_input()
    start_time = time.time()
    print(foo(data, _filter))
    print("--- %s seconds ---" % (time.time() - start_time))
