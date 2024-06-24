from sys import stdin


s = input().strip()
fn_lst = []
for fn in stdin:
    fn_lst.append(fn.rstrip())

ans = []
for fn in fn_lst:
    q_arr = []
    with open(fn, encoding="UTF-8") as f:
        for line in f:
            for q_str in line.rstrip().split():
                if q_str:
                    q_arr.append(q_str.lower())

        if s.lower() in ' '.join(q_arr):
            ans.append(fn)
if ans:
    print('\n'.join(ans))
else:
    print("404. Not Found")
