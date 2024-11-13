import string

user_input = input("Введіть дві літери через дефіс: ")

str_ascii = string.ascii_letters

str_start = str_ascii.index(user_input[0])
str_end = str_ascii.index(user_input[-1])

print(str_ascii[str_start:str_end + 1])    

