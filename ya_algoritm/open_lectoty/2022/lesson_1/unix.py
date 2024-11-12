"""B. Канонический путь"""

"""https://contest.yandex.ru/contest/39359/problems/B/"""

path = input().strip()


build_paths = []
arr = path.split("/")

for _, ch in enumerate(arr):
    if not ch:
        continue

    if ch == "..":
        l = len(build_paths)
        if l > 0:
            build_paths.pop()
    elif ch != ".":
        build_paths.append(ch)


print(f"/{'/'.join(build_paths)}")
