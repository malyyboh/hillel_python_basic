user_number = int(input("Введіть 5-ти значне число: "))

fifth_digit = str(user_number % 10)
fourth_digit = str(user_number // 10 % 10)
third_digit = str(user_number // 100 % 10)
second_digit = str(user_number // 1000 % 10)
first_digit = str(user_number // 10000)

print(fifth_digit + fourth_digit + third_digit + second_digit + first_digit)
