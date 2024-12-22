from Person import *
from colorama import Fore, Back, Style
import codecs


print(f"{Fore.BLACK}{Back.LIGHTWHITE_EX}Програма для роботи з даними про людей{Style.RESET_ALL}")

all_records = DataPersons()

while True:
    print(f"{Fore.LIGHTCYAN_EX}{Back.BLACK}Введіть відповідну команду для роботи з даними:{Style.RESET_ALL}")
    print(f"1) для додавання нового запису введіть:{Fore.LIGHTRED_EX} add{Style.RESET_ALL}")
    print(f"2) для пошуку в доданих записах по імені, прізвищу чи по-батькові введіть:{Fore.LIGHTRED_EX} search{Style.RESET_ALL}")
    print(f"3) для збереження введених даних до файлу данних введіть:{Fore.LIGHTRED_EX} save{Style.RESET_ALL}")
    print(f"4) для пошуку записів в файлі по імені, прізвищу чи по-батькові введіть:{Fore.LIGHTRED_EX} search in file{Style.RESET_ALL}")
    print(f"5) для переляду всіх доданих записів введіть:{Fore.LIGHTRED_EX} show all{Style.RESET_ALL}")
    print(f"6) для переляду всіх записів з файлу введіть:{Fore.LIGHTRED_EX} show all in file{Style.RESET_ALL}")
    print(f"7) для виходу з програми введіть:{Fore.LIGHTRED_EX} exit{Style.RESET_ALL}")
    user_input = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть команду:{Style.RESET_ALL} ")

    def add_person():
        name = input("Введіть імя: ").title()
        birthday = input("Введіть дату народження: ")
        gender = input("Введіть стать (чоловік чи жінка): ")
        last_name = input("Введіть прізвище (щоб пропустити натисніть Enter): ").title()
        father_name = input("Введіть по-батькові (щоб пропустити натисніть Enter): ").title()
        date_of_death = input("Введіть дату смерті (щоб пропустити натисніть Enter): ")
        obj = Person(name=name, birthday=birthday, gender="m" if gender == "чоловік" else "f", last_name="-" if last_name=='' else last_name, father_name='-' if father_name=='' else father_name, date_of_death='-' if  date_of_death=='' else  date_of_death)
        obj.correct_date()
        all_records.add_person(obj)

    def search_added_person(records: DataPersons):
        if records.data_persons:
            user_search = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть імя, прізвище чи по-батькові:{Style.RESET_ALL} ").title()
            user_search_lst = user_search.split()
            find_records_print = all_records.find_person(*user_search_lst)
            if not find_records_print:
                user_search = input(f"{Fore.LIGHTRED_EX}Дані відустні! Продовжити пошук? (Yes or No):{Style.RESET_ALL} ")
                if user_search.lower() == "yes":
                    return search_added_person(all_records)
            else:
                return print(f"{Fore.LIGHTGREEN_EX}{find_records_print}")
        else:
            return print(f"{Fore.LIGHTRED_EX}Жодних доданих записів для пошуку не має! Спочатку додайте дані!{Style.RESET_ALL}")

    def save_person(records: DataPersons):
        if records.data_persons:
            input_file_name = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Задайте назву текстового файлу для збереження:{Style.RESET_ALL} ")
            with codecs.open(f"db/{input_file_name}.txt", "a", "utf-8") as db:
                for item in records.data_persons:
                    db.write(f"{str(item)}\n")
            save_message = f"{Fore.LIGHTGREEN_EX}Дані збережено!{Style.RESET_ALL}"
        else:
            save_message = f"{Fore.LIGHTRED_EX}Дані для збереження відсутні!{Style.RESET_ALL}"
        return print(save_message)

    def search_person():
        input_file_name = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть назву файлу для пошуку:{Style.RESET_ALL} ")
        try:
            with codecs.open(f"db/{input_file_name}.txt", "r", "utf-8") as db:
                db_lines = db.readlines()
        except FileNotFoundError:
            print(f"{Fore.LIGHTRED_EX}Файла не знайдено!{Style.RESET_ALL}")

        else:
            find_records = DataPersons()
            user_search = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть імя, прізвище чи по-батькові:{Style.RESET_ALL} ").title()
            user_search_lst = user_search.split()
            find_records_print = ""
            for line in db_lines:
                args = line.split()
                find_obj = Person(*args)
                find_records.add_person(find_obj)
                find_records_print = find_records.find_person(*user_search_lst)
            if not find_records_print:
                user_search = input(f"{Fore.LIGHTRED_EX}Дані відустні! Продовжити пошук? (Yes or No):{Style.RESET_ALL} ")
                if user_search.lower() == "yes":
                    return search_person()
            else:
                return print(f"{Fore.LIGHTGREEN_EX}{find_records_print}")

    def show_all_added_persons(records: DataPersons):
        if records.data_persons:
            return print(f"{Fore.LIGHTGREEN_EX}{records.__str__()}")
        else:
            return print(f"{Fore.LIGHTRED_EX}Дані для перегляду відсутні! Спочатку додайте дані!{Style.RESET_ALL}")

    def show_all_persons():
        input_file_name = input(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}Введіть назву файлу для відображення всіх записів:{Style.RESET_ALL} ")
        try:
            with codecs.open(f"db/{input_file_name}.txt", "r", "utf-8") as db:
                db_lines = db.readlines()
        except FileNotFoundError:
            print(f"{Fore.LIGHTRED_EX}Файла не знайдено!{Style.RESET_ALL}")
        else:
            all_records_in_file = DataPersons()
            for line in db_lines:
                args = line.split()
                record_obj = Person(*args)
                all_records_in_file.add_person(record_obj)

            if not all_records_in_file.data_persons:
                print(f"{Fore.LIGHTRED_EX}В даному файлі не має жодного запису!{Style.RESET_ALL} ")
            else:
                return print(f"{Fore.LIGHTGREEN_EX}{all_records_in_file.__str__()}")

    def exit_prog():
        if all_records.data_persons:
            save_input = input(f"{Fore.LIGHTRED_EX}Введені дані не збережені! Введіть 'save' для збереження або 'not save', щоб вийти без збереження:{Style.RESET_ALL} ")
            if save_input.lower() == "save":
                save_person(all_records)
        exit()


    if user_input.lower() == "add":
        add_person()

    if user_input.lower() == "search":
        search_added_person(all_records)

    if user_input.lower() == "save":
        save_person(all_records)
        all_records = DataPersons()

    if user_input.lower() == "search in file":
        search_person()

    if user_input.lower() == "show all":
        show_all_added_persons(all_records)

    if user_input.lower() == "show all in file":
        show_all_persons()

    if user_input.lower() == "exit":
        exit_prog()

    if user_input.lower() not in ["add", "search", "save", "search in file", "show all", "show all in file", "exit"]:
        print(f"{Fore.LIGHTRED_EX}Неправильна назва команди!{Style.RESET_ALL}")






