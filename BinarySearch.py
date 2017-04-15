inp = [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 17, 20, 22]
target = 17

c = 0
s = 0
e = len(inp) - 1

while inp[c] is not target and s is not e:
    c = (s + e) / 2
    if inp[c] is target:
        print c
    elif inp[c] < target:
        s = c
    elif inp[c] > target:
        e = c
    else:
        print -1
