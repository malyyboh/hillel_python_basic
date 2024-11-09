import string

user_str = input("Please input a string: ")
str_punctuation = string.punctuation
hashtag_mark = "#"

for item in user_str:
    if item in str_punctuation:
        user_str = user_str.replace(item, '')

user_str = hashtag_mark + user_str.title().replace(' ', '')

if len(user_str) > 140:
    user_str = user_str[:141]

print(user_str)
