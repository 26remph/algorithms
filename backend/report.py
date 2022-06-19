from typing import List, Tuple, Optional, Dict, Union
import json
import time


def judge(element, _filter):

    f_1 = _filter['NAME_CONTAINS'] in element['name']
    f_2 = element['price'] >= int(_filter['PRICE_GREATER_THAN'])
    f_3 = element['price'] <= int(_filter['PRICE_LESS_THAN'])

    date = time.strptime(element['date'], '%d.%m.%Y')
    date_after = time.strptime(_filter['DATE_AFTER'], '%d.%m.%Y')
    date_before = time.strptime(_filter['DATE_BEFORE'], '%d.%m.%Y')
    f_4 = date_after <= date <= date_before

    is_judge = all([f_1, f_2, f_3, f_4])

    if is_judge:
        _filter['match'] += 1

    return is_judge


def foo(input_dict, _filter) -> str:

    output_dict: list = sorted(
        input_dict, key=lambda x: (-judge(x, _filter), x['id'])
    )

    count = _filter['match']
    return json.dumps(output_dict[:count])


def read_input() -> Tuple[dict, Dict[str, Union[str, int]]]:

    input_dict = json.loads(input())
    # with open('input_report.json') as f:
    #     input_dict = json.load(f)

    _filter: Dict[str, Union[str, int]] = {'match': 0}
    # for _ in range(5):
    #     key, val = input().split()
    #     _filter[key] = val

    with open('input_report.txt') as f:
        for _ in range(5):
            key, val = f.readline().split()
            _filter[key] = val

    return input_dict, _filter


if __name__ == '__main__':
    data, _filter = read_input()
    # start_time = time.time()
    print(foo(data, _filter))
    # print("--- %s seconds ---" % (time.time() - start_time))
