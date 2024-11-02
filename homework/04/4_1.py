lst = [1, 0, 13, 0, 0, 0, 5]

for i in lst:
    if i == 0:
        lst.remove(i)
        lst.append(i)
print(lst)