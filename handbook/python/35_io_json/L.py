with (
    open(input()) as f,
    open(input(), 'w', encoding="UTF-8") as f_even,
    open(input(), 'w', encoding="UTF-8") as f_odd,
    open(input(), 'w', encoding="UTF-8") as f_eq,
):
    for line in f:
        for num in line.split():
            cnt = sum((1 if int(ch) % 2 == 0 else -1 for ch in num))
            if cnt > 0:
                f_even.write(num + ' ')
            elif cnt < 0:
                f_odd.write(num + ' ')
            else:
                f_eq.write(num + ' ')

            print(f"{num=}", f"{cnt=}", f"len_num={len(num)}")

        for fw in (f_even, f_odd, f_eq):
            fw.write("\n")
