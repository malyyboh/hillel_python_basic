import random

lst = []
lst_2 = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 10))
print(lst)

for i, el in enumerate(lst):
    if i == 0 or i == 2 or i == len(lst) - 2:
        lst_2.append(el)
print(lst_2)
