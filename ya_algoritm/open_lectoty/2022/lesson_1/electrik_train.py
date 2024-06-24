"""
Летние школы Академии Яндекса 2022.
Занятие 1 (Разбор случаев, линейный поиск)

D. Разница во времени
"""

from datetime import datetime, timedelta


# def slow_f(arr):
#
#     min_t = 1440
#     if len(arr) <= 1:
#         min_t = 0
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i == j:
#                 continue
#
#             frm = "%H:%M"
#             t1 = datetime.strptime(arr[i], frm)
#             t2 = datetime.strptime(arr[j], frm)
#             tdelta = t2 - t1
#             if tdelta.days < 0:
#                 tdelta = timedelta(days=0, seconds=tdelta.seconds)
#             min_t = min(min_t, tdelta.seconds // 60)
#     return min_t


def diff_time_in_minutes(s1: str, s2: str):
    frm = "%H:%M"
    t1 = datetime.strptime(s1, frm)
    t2 = datetime.strptime(s2, frm)
    t_delta = t2 - t1
    if t_delta.days < 0:
        t_delta = timedelta(days=0, seconds=t_delta.seconds)

    return t_delta.seconds // 60


n = int(input())
arr = list(input().split())

arr.sort()

min_t = 0
if len(arr) > 1:
    min_t = diff_time_in_minutes(arr[-1], arr[0])

i = 0
while i < len(arr) - 1:
    min_t = min(min_t, diff_time_in_minutes(arr[i], arr[i + 1]))
    i += 1

print(min_t)

# print(slow_f(arr))
# arr = ['00:00', '23:59', '00:30', '21:05', '05:00', '06:00', '23:10']
# arr = ['00:00', '12:00', '00:30', '21:05', '05:00', '06:00', '23:10']
# arr = ['00:00']
# arr = ['00:00', '23:59', '00:00']
# arr = ['23:59', '00:00']
# arr = ['00:00', '12:01']