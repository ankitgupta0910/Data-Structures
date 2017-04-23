s = "My name is Ankit "
r = ""
t = []
l = len(s)
tl = 0

for i in s:
    if i is not " " and tl is not l:
        t.append(i)
    else:
        for j in reversed(t):
            r = r + j
        r = r + " "
        t = []
    tl += 1
print r
