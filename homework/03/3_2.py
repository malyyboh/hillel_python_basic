example_list = [1, 2, 3]

if len(example_list) > 1:
    example_list.insert(0, example_list[-1])
    example_list.pop()
    print(example_list)
else:
    print(example_list)
