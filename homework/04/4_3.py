import random

lst = []
new_lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 10))
print(lst)

for i, el in enumerate(lst):
    if i == 0 or i == 2 or i == len(lst) - 2:
        new_lst.append(el)
print(new_lst)
