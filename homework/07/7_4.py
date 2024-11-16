def common_elements():
    first_list = [i for i in range(0, 100) if i % 3 == 0]
    second_list = [i for i in range(0, 100) if i % 5 == 0]
    intersection_set = set(first_list).intersection(set(second_list))
    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
