from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        """Interface method"""


class Student(IPerson):

    def __init__(self):
        self.name = "Student"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    def build_person(p_type):
        if p_type == "Student":
            return Student()
        elif p_type == "Teacher":
            return Teacher()
        else:
            print("Invalid type")
            return -1


if __name__ == '__main__':

    # normal object creation
    s1 = Student()
    s1.person_method()

    t1 = Teacher()
    t1.person_method()

    # factory design pattern
    choice = input("Teacher or Student: ")
    person = PersonFactory.build_person(choice)
    person.person_method()
