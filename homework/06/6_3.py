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





# last_digit = user_int_input % 10
# second_digit = user_int_input // 10 % 10
# first_digit = user_int_input // 100 % 10
# print(len(str(user_int_input)))
# i = 0
# while len(str(user_int_input)) >= i:
#     user_int_input = int(last_digit * second_digit * first_digit)
#     i += 1
#     print(user_int_input)


# int_list = list()
# result_int = 1
#
# for item in user_int_input:
#     int_list.append(int(item))
#     result_int *= int(item)
#
# while len(int_list) >= 1:
#     result_int *= item
# print(int_list)
# print(result_int)

