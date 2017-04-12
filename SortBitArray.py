a = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

l = len(a)

s = 0
e = l-1
i = 0

while s < e:
    while a[s] is not 1:
        s += 1
    while a[e] is not 0:
        e -= 1
    if s < e:
        t = a[s]
        a[s] = a[e]
        a[e] = t

print a
