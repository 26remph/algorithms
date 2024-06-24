import datetime
import math


frm = '%H:%M:%S'
a = datetime.datetime.strptime(input().strip(), frm)
b = datetime.datetime.strptime(input().strip(), frm)
c = datetime.datetime.strptime(input().strip(), frm)
delay = math.ceil((c - a).seconds / 2)
ans = b + datetime.timedelta(seconds=delay)
print(ans.strftime(frm))
