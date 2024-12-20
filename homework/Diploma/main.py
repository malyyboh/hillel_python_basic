from Person import *
from colorama import Fore, Back, Style
import codecs


print(f"{Fore.LIGHTCYAN_EX}РОБОТА З БАЗОЮ ДАНИХ ЛЮДЕЙ{Style.RESET_ALL}")

all_records = DataPersons()

while True:
    print(f"{Fore.LIGHTYELLOW_EX}Введіть відповідну команду для роботи з базою даних:{Style.RESET_ALL}")
    print(f"1) для додавання нового запису введіть:{Fore.LIGHTRED_EX} add{Style.RESET_ALL}")
    print(f"2) для збереження введених даних данних введіть:{Fore.LIGHTRED_EX} save{Style.RESET_ALL}")
    print(f"3) для пошуку запису по імені, прізвищу чи по-батькові введіть:{Fore.LIGHTRED_EX} search{Style.RESET_ALL}")
    print(f"4) для переляду всіх записів з бази даних введіть:{Fore.LIGHTRED_EX} show all{Style.RESET_ALL}")
    print(f"5) для виходу з програми введіть:{Fore.LIGHTRED_EX} exit{Style.RESET_ALL}")
    user_input = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть команду:{Style.RESET_ALL} ")

    def add_person():
        name = input("Введіть імя: ").title()
        birthday = input("Введіть дату народження: ")
        gender = input("Введіть стать (чоловік чи жінка): ")
        last_name = input("Введіть прізвище (щоб пропустити натисніть Enter): ").title()
        father_name = input("Введіть по-батькові (щоб пропустити натисніть Enter): ").title()
        date_of_death = input("Введіть дату смерті (щоб пропустити натисніть Enter): ")
        obj = Person(name=name, birthday=birthday, gender='m' if gender == "чоловік" else "f", last_name=last_name, father_name=father_name, date_of_death=date_of_death)
        obj.correct_date()
        all_records.add_person(obj)

    def save_person(records: DataPersons):
        if records.data_persons:
            with codecs.open('db.txt', 'a', 'utf-8') as db:
                for item in records.data_persons:
                    db.write(f"{str(item)}\n")
            save_message = f"{Fore.LIGHTGREEN_EX}Дані збережено!{Style.RESET_ALL}"
        else:
            save_message = f"{Fore.LIGHTRED_EX}Дані для збереження відсутні!{Style.RESET_ALL}"
        return print(save_message)

    def search_person():
        with codecs.open('db.txt', 'r', 'utf-8') as db:
            db_lines = db.readlines()
        find_records = DataPersons()
        user_search = input("Введіть імя, прізвище чи по-батькові: ").title()
        for line in db_lines:
            args = line.split()
            find_obj = Person(*args)
            find_records.add_person(find_obj)
        return print(find_records.find_person(user_search))

    def exit_prog():
        if all_records.data_persons:
            save_input = input("Введена дані не збережені! Введіть 'save' для збереження або 'not save', щоб вийти без збереження: ")
            if save_input.lower() == "save":
                save_person(all_records)
        exit()

    if user_input.lower() == "add":
        add_person()

    if user_input.lower() == "save":
        save_person(all_records)
        all_records = DataPersons()

    if user_input.lower() == "search":
        search_person()

    if user_input.lower() == "exit":
        exit_prog()

    # if user_input == "show all":
    #     with codecs.open('db.txt', 'r', 'utf-8') as db:
    #         db_lines = db.readlines()
    #         args = []
    #         for line in db_lines:
    #             args = line.split()
    #             obj = Person(*args)
    #             print(obj.__str__())





