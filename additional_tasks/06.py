
user_input_first_bool = input("Please input first logical value (True or False): ")
user_input_second_bool = input("Please input second logical value (True or False): ")

if user_input_first_bool == "True":
    user_input_first_bool = bool(1)
else:
    user_input_first_bool = bool(0)

if user_input_second_bool == "True":
    user_input_second_bool = bool(1)
else:
    user_input_second_bool = bool(0)

print("Logical AND:", user_input_first_bool and user_input_second_bool)
print("Logical OR:", user_input_first_bool or user_input_second_bool)
print("Logical NOT:", not user_input_first_bool, not user_input_second_bool)
print("Comparing two values for equality:", user_input_first_bool == user_input_second_bool)
print("Comparing two values for inequality:", user_input_first_bool != user_input_second_bool)
