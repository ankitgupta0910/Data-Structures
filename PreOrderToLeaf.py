a = [50, 30, 20, 5, 10, 15, 25, 40, 35, 70, 60, 55, 65, 80, 75, 85]


def func(a):
    l = []
    r = []
    if len(a) is not 1:
        for i in a[1:]:
            if i < a[0]:
                l.append(i)
            else:
                r.append(i)
        if len(l) > 0:
            func(l)
        if len(r) > 0:
            func(r)
        # print l
        # print r
    else:
        print a[0]

func(a)
