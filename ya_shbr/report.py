import json
import time

from typing import Dict, Tuple, Union


def judge(element, _filter):

    f_1 = _filter['NAME_CONTAINS'] in element['name']
    f_2 = element['price'] >= int(_filter['PRICE_GREATER_THAN'])
    f_3 = element['price'] <= int(_filter['PRICE_LESS_THAN'])

    date = time.strptime(element['date'], '%d.%m.%Y')
    date_after = time.strptime(_filter['DATE_AFTER'], '%d.%m.%Y')
    date_before = time.strptime(_filter['DATE_BEFORE'], '%d.%m.%Y')
    f_4 = date_after <= date <= date_before

    is_allowed = all([f_1, f_2, f_3, f_4])

    if is_allowed:
        _filter['match'] += 1

    return is_allowed


def foo(input_dict, _filter) -> str:

    if not input_dict:
        return json.dumps({})

    if len(input_dict) == 1 and not input_dict[0]:
        return json.dumps({})

    output_dict: list = sorted(
        input_dict, key=lambda x: (-judge(x, _filter), x['id'])
    )

    count = _filter['match']

    if count > 0:
        return json.dumps(output_dict[:count])
    else:
        return json.dumps({})


def read_input() -> Tuple[dict, Dict[str, Union[str, int]]]:

    json_str = input()
    if json_str:
        input_dict = json.loads(json_str)
    else:
        input_dict = json.loads('{}')

    _filter: Dict[str, Union[str, int]] = {'match': 0}
    for _ in range(5):
        key, val = input().split()
        _filter[key] = val

    return input_dict, _filter


data, _filter = read_input()
print(foo(data, _filter))
