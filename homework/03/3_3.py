user_list = [1, 2, 3, 4, 5, 6]

first_list = []
second_list = []
divided_user_list = []
new_user_list = []

if len(user_list) == 0:
    new_user_list = [first_list] + [second_list]
    print(new_user_list)
elif len(user_list) % 2 == 0:
    divided_user_list = len(user_list) // 2
    first_list = user_list[:divided_user_list]
    second_list = user_list[divided_user_list:]
    new_user_list = [first_list] + [second_list]
    print(new_user_list)
else:
    divided_user_list = round(len(user_list) / 2 + 0.1)
    first_list = user_list[:divided_user_list]
    second_list = user_list[divided_user_list:]
    new_user_list = [first_list] + [second_list]
    print(new_user_list)
