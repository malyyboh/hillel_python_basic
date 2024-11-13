user_int_input = (input("Введіть ціле число: "))

item = 1

while True:
    for i in user_int_input:
        item *= int(i)
    user_int_input = str(item)
    item = 1
    if int(user_int_input) <= 9:
        break
print(user_int_input)


