import json
import time


def gatekeeper(element, _filter):

    nc = _filter['NAME_CONTAINS'].lower()
    el_name = element['name'].lower()

    f_1 = nc in el_name
    f_2 = element['price'] >= int(_filter['PRICE_GREATER_THAN'])
    f_3 = element['price'] <= int(_filter['PRICE_LESS_THAN'])

    date = time.strptime(element['date'], '%d.%m.%Y')
    date_after = time.strptime(_filter['DATE_AFTER'], '%d.%m.%Y')
    date_before = time.strptime(_filter['DATE_BEFORE'], '%d.%m.%Y')
    f_4 = date_after <= date <= date_before

    is_true = all([f_1, f_2, f_3, f_4])

    if is_true:
        _filter['match'] += 1

    return is_true


def foo(input_dict, _filter):

    if not input_dict:
        return json.dumps({})

    if len(input_dict) == 1 and not input_dict[0]:
        return json.dumps({})

    out_data: list = sorted(
        input_dict, key=lambda x: (-gatekeeper(x, _filter), x['id'])
    )

    count = _filter['match']

    if count > 0:
        return json.dumps(out_data[:count])
    else:
        return json.dumps({})


def read_input():

    inp_data = json.loads(input())

    inp_filter = {'match': 0}
    for _ in range(5):
        key, val = input().split()
        inp_filter[key] = val

    return inp_data, inp_filter


data, _filter = read_input()
print(foo(data, _filter))
