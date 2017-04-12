a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 19

s = 0
e = len(a) - 1
i = 0

while s is not e:
    if a[s] + a[e] > t:
        e -= 1
    elif a[s] + a[e] < t:
        s += 1
    else:
        print s, e
        break
    if s is e:
        print False
    i += 1
