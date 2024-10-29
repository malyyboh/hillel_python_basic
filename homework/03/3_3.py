user_list = [1, 2, 3, 4, 5, 6]

divided_paired_user_list = len(user_list) // 2
divided_odd_user_list = round(len(user_list) / 2 + 0.1)

if len(user_list) % 2 == 0:
    first_list = user_list[:divided_paired_user_list]
    second_list = user_list[divided_paired_user_list:]
else:
    first_list = user_list[:divided_odd_user_list]
    second_list = user_list[divided_odd_user_list:]

new_user_list = [first_list] + [second_list]
print(new_user_list)
