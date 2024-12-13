class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        human_str = super().__str__()
        return f"{human_str} {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise MaxNumberOfStudent

    def delete_student(self, last_name):
        student_for_delete = self.find_student(last_name)
        if student_for_delete:
            if last_name == student_for_delete.last_name:
                return self.group.discard(student_for_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += str(f"{i} ")
        return f'Number:{self.number}\n{all_students} '


class MaxNumberOfStudent(Exception):
    pass


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Male', 25, 'John', 'Swift', 'AN145')
st3 = Student('Female', 23, 'Ann', 'Berg', 'AN145')
st4 = Student('Female', 22, 'Megan', 'Rich', 'AN145')
st5 = Student('Male', 25, 'Mark', 'Zuckerberg', 'AN145')
st6 = Student('Male', 26, 'Jake', 'Brenton', 'AN145')
st7 = Student('Female', 25, 'Viktoria', 'Manson', 'AN145')
st8 = Student('Male', 22, 'Michal', 'Billing', 'AN145')
st9 = Student('Female', 25, 'Rachel', 'Bricks', 'AN145')
st10 = Student('Female', 27, 'Monica', 'Bellucci', 'AN145')
st11 = Student('Male', 27, 'Jane', 'Branson', 'AN145')
print(st1)

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except MaxNumberOfStudent:
    print("Maximum number of students in a group is 10!")

print(gr)
gr.find_student('Jobs')
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
#
gr.delete_student('Taylor')  # No error!

