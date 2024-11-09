# simple calculator
prop_user_message = "yes"

while prop_user_message == "yes":
    user_first_number = float(input("Введіть перше число: "))
    user_second_number = float(input("Введіть друге число: "))
    user_math_operation = input("Введіть одну з математичних операцій (+, -, *, /): ")
    if user_math_operation == "+":
        print(user_first_number + user_second_number)
    elif user_math_operation == "-":
        print(user_first_number - user_second_number)
    elif user_math_operation == "*":
        print(user_first_number * user_second_number)
    elif user_math_operation == "/":
        if user_second_number != 0:
            print(user_first_number / user_second_number)
        else:
            print("Ділити на нуль заборонено!")
    else:
        print("Калькулятор не підтримує таку операцію!")
    prop_user_message = input("Чи продовжити обчислення? (якщо так, введіть 'yes') ")



