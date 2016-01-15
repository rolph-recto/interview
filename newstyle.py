#!/usr/bin/env python
# newstyle.py
# new-style classes

class Student(object):
    def __init__(self, name, grade):
        self._name = ''
        self._grade = -1
        self.name = name
        self.grade = grade

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print 'Student name must be a string!'
            
        elif len(new_name) == 0:
            print 'Student name cannot be empty string!'

        else:
            elf._name = new_name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if not isinstance(new_grade, int):
            print 'Student grade must be an integer!'

        elif new_grade < 1 or new_grade > 12:
            print 'Student grade must be between 1 and 12!'

        else:
            self._grade = new_grade

def main():
    a = Student('Alice', 11)
    b = Student('Bob', 9)

    print a.name
    a.name = 10
    print a.name


if __name__ == '__main__':
    main()
