from datetime import date, datetime


class DataPersons:
    def __init__(self):
        self.data_persons = set()

    def __str__(self):
        all_persons = ""
        for person in self.data_persons:
            all_persons += (f"{person.name} {person.last_name if person.last_name != '-' else ''} {person.father_name if person.father_name != '-' else ''} "
                            f"{person.calc_age()}, {'чоловік.' if person.gender == 'm' else 'жінка.'} {'Народився' if person.gender == 'm' else 'Народилася'} {person.birthday}. "
                            f"{'Помер' if person.gender == 'm' and person.date_of_death != '-' else 'Померла' if person.gender == 'f' and person.date_of_death != '-' else ''} {person.date_of_death + '.' if person.date_of_death != '-' else ''}\n")
        return all_persons

    def add_person(self, person):
        self.data_persons.add(person)

    def find_person(self, *args):
        find_person_str_lst = []
        for person in self.data_persons:
            for i in args:
                if i in person.name or i in person.last_name or i in person.father_name:
                    find_person_str = (f"{person.name} {person.last_name if person.last_name != '-' else ''} {person.father_name if person.father_name != '-' else ''} "
                                       f"{person.calc_age()}, {'чоловік.' if person.gender == 'm' else 'жінка.'} {'Народився' if person.gender == 'm' else 'Народилася'} {person.birthday}. "
                                       f"{'Помер' if person.gender == 'm' and person.date_of_death != '-' else 'Померла' if person.gender == 'f' and person.date_of_death != '-' else ''} {person.date_of_death + '.' if person.date_of_death != '-' else ''}\n")
                    if find_person_str not in find_person_str_lst:
                        find_person_str_lst.append(find_person_str)
        find_person = ''
        for person_item in find_person_str_lst:
            find_person += person_item
        return find_person


class Person:
    def __init__(self, name, birthday, gender, last_name='-', father_name='-', date_of_death='-'):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.last_name = last_name
        self.father_name = father_name
        self.date_of_death = date_of_death

    def __str__(self):
        return f"{self.name} {self.birthday} {self.gender} {self.last_name} {self.father_name} {self.date_of_death}"

    def correct_date(self):
        self.birthday = self.birthday.strip()
        for i in self.birthday:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.birthday = self.birthday.replace(i, ".")
        if self.date_of_death != "-":
            self.date_of_death = self.date_of_death.strip()
            for i in self.date_of_death:
                if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.date_of_death = self.date_of_death.replace(i, ".")

    def calc_age(self):
        birthday_date_lst = self.birthday.split('.')
        birthday = datetime(int(birthday_date_lst[2]), int(birthday_date_lst[1]), int(birthday_date_lst[0]))

        if self.date_of_death == "-":
            today = date.today()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        else:
            death_date_lst = self.date_of_death.split('.')
            death_date = datetime(int(death_date_lst[2]), int(death_date_lst[1]), int(death_date_lst[0]))
            age = death_date.year - birthday.year - (
                    (death_date.month, death_date.day) < (birthday.month, birthday.day))

        if age % 10 == 1:
            if age == 11:
                age = f"{age} років"
            else:
                age = f"{age} рік"
        elif age % 10 in [2, 3, 4]:
            if age in [12, 13, 14]:
                age = f"{age} років"
            else:
                age = f"{age} роки"
        elif age % 10 in [0, 5, 6, 7, 8, 9]:
            age = f"{age} років"

        return age
