m = [[2, 3, 4], [5, 6, 7]]
r = []
h = len(m)
w = len(m[0])
i=0
j=h-1
while i < w:
    t = []
    while j >= 0:
        # print m[j][i],
        t.append(m[j][i])
        j -= 1
    # print "\r"
    r.append(t)
    j=h-1
    i += 1
print r
