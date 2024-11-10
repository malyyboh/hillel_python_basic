import keyword

user_string = input('Please input a variable name: ')

if user_string.isidentifier():
    if user_string not in keyword.kwlist and user_string.islower() and user_string.count('_') <= 1:
        print(True)
    else:
        if user_string == '_':
            print(True)
        else:
            print(False)
else:
    print(False)

