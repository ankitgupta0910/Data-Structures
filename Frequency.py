a = [11, 21, 31, 11, 21, 31, 41, 51]
d = {}

for i in a:
    d[i] = d.get(i, 0) + 1

print d.items()
