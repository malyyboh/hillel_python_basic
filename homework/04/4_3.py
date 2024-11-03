import random

lst = []
new_lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 10))
print(lst)

new_lst.append(lst[0])
new_lst.append(lst[2])
new_lst.append(lst[-2])

print(new_lst)

