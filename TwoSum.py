num = [4, 2, 6, 5, 7, 9, 10]
target = 13
temp = {}

for i in range(len(num)):
    if temp.get(num[i], False):
        print True
        break
    temp[target - num[i]] = True
print False
