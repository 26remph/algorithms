N = int(input())
titles = []
for _ in range(N):
    titles.append(input())

query = input().lower()
for t in titles:
    if query in t.lower():
        print(t)
