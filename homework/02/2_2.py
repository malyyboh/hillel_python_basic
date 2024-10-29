user_number = int(input("Введіть 5-ти значне число: "))

fifth_digit = (user_number % 10) * 10000
fourth_digit = (user_number // 10 % 10) * 1000
third_digit = (user_number // 100 % 10) * 100
second_digit = (user_number // 1000 % 10) * 10
first_digit = (user_number // 10000)

print(fifth_digit + fourth_digit + third_digit + second_digit + first_digit)
