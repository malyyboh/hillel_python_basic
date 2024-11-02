lst = [0, 1, 7, 2, 4, 8]
sum_elements = 0

for i in lst:
    if lst.index(i) % 2 == 0:
        sum_elements = sum_elements + i

if sum_elements > 0:
    sum_elements = sum_elements * lst[-1]
    print(sum_elements)
else:
    print(0)


