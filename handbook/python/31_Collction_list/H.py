N = int(input())
for _ in range(N):
    s = input().lower()
    index = s.find("зайка")
    if index != -1:
        print(index + 1)
    else:
        print("Заек нет =(")
