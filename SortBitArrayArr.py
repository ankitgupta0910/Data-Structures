a = [0, 1, 1, 0, 1, 1, 1, 0]
r = [0, 0]

for i in range(len(a)):
    if a[i] is 0:
        r[0] = r[0] + 1
    else:
        r[1] = r[1] + 1

del a[:]

a += [0] * r[0]
a += [1] * r[1]

print a
