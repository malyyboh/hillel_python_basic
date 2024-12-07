# Написати програму, яка просить ввести 4 числа – кількість днів, годин,
# хвилин і секунд. Програма виводить цей час у секундах.

user_input_days = int(input("Please input number of days: "))
user_input_hours = int(input("Please input number of hours: "))
user_input_minutes = int(input("Please input number of minutes: "))
user_input_seconds = int(input("Please input number of seconds: "))

sum_seconds = (user_input_days * 24 * 3600) + (user_input_hours * 3600) + (user_input_minutes * 60) + user_input_seconds
print(sum_seconds)