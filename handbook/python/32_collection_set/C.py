N = int(input())
area = set()
for _ in range(N):
    area.update(input().split())
print("\n".join(area))
