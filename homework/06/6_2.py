user_sec_input = int(input("Введіть число від 0 до 8640000: "))

days = user_sec_input // 60 // 60 // 24
hours = (user_sec_input // 60 // 60) % 24
minutes = (user_sec_input // 60) % 60
seconds = user_sec_input % 60

if days % 10 == 1:
    if days == 11:
        print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    else:
        print(f"{days} день, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
elif days % 10 in [2, 3, 4]:
    if days in [12, 13, 14]:
        print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    else:
        print(f"{days} дні, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
elif days % 10 in [0, 5, 6, 7, 8, 9]:
    print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

