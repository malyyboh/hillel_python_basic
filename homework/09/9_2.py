def difference(*args):
    if len(args) > 1:
        return round(max(args) - min(args), 2)
    elif len(args) == 1:
        return args  # return the element without changes
    else:
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
