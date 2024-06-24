N1, N2 = input(), input()
total = int(N1[0]) + int(N2[0]) + int(N1[1]) + int(N2[1])
pos1 = max(N1 + N2)
pos2 = min(N1 + N2)
mid = str(total - int(pos1) - int(pos2))
mid = mid[1] if len(mid) == 2 else mid[0]
print(pos1 + mid + pos2)
