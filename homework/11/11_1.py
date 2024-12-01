def prime_generator(end):
    start = 2
    non_prime_number = 0
    while start <= end:
        for i in range(2, end + 1):
            if start % i == 0 and start != i:
                non_prime_number = start
                break
        if non_prime_number != start:
            yield start
        start += 1


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')




