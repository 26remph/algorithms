import json

fn_in = input()
fn_out = input()

with open(fn_in, encoding="UTF-8") as f:

    count = 0
    pos_count = 0
    min_n = float("inf")
    max_n = float("-inf")
    summa = 0

    for line in f:
        for n in line.rstrip().split():
            try:
                conv_n = float(n)
            except ValueError:
                continue
            count += 1
            pos_count += 1 if conv_n > 0 else 0
            min_n = min(min_n, conv_n)
            max_n = max(max_n, conv_n)
            summa += conv_n

avg = summa / count if count else 0
out = {
    "count": int(count),
    "positive_count": int(pos_count),
    "min": int(min_n),
    "max": int(max_n),
    "sum": int(summa),
    "average": f'{avg:.2f}'
}

with open(fn_out, "w", encoding="UTF-8") as f:
    json.dump(out, f)

print(out)






