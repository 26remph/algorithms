import json


fn = input()
with (
    open(fn, "rw+", encoding="UTF-8") as f_in,
    open(input(), encoding="UTF-8") as f_upd,
):
    out_dict = {}
    for d in json.load(f_in):
        key = d.get("name")
        del d["name"]
        out_dict[key] = dict(d)

    for d in json.load(f_upd):
        key = d.get("name")
        del d["name"]
        info = out_dict.get(key, {})

        for k, v in d.items():
            if k in info:
                if str(v) > str(info[k]):
                    info[k] = v
            else:
                info[k] = v

        out_dict[key] = info

with open(fn, "w", encoding="UTF-8") as f:
    json.dump(out_dict, f)
