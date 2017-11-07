# -*- coding: utf-8 -*-
#Homework09 - Author Maha

from collections import defaultdict
from prettytable import PrettyTable

def file_reader(f, no_of_args):
    """open file f, reads line by line, and yield one line at a time"""

    try:
        data = open(f)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    else:
        with data:
            for line in data:
                if len(line.strip().split('\t')) == no_of_args:
                    yield line.strip().split('\t')
                else:
                    raise ValueError('incorrect line format')

class Repository:
    """hold the students, instructors and grades"""

    def __init__(self):
        """intiate an empty dict for students and instructors"""
        self.students = dict()
        self.instructors = dict()
        #self.grades= list()
    
    def read_students_file(self, f, no_of_args):
        """read students file and store students data in dict"""
        for cwid, name, major in file_reader(f, no_of_args):
            self.students[cwid] = Student(cwid, name, major)

    def read_instructors_file(self, f, no_of_args):
        """read instructors file and store instructor data in dict"""
        for cwid, name, dept in file_reader(f, no_of_args):
            self.instructors[cwid]= Instructor(cwid, name, dept)

    def read_grades_file(self, f, no_of_args):
        """read grades file and assign courses to students and instructors"""
        for std_cwid, course, ltr_grade, ins_cwid in file_reader(f, no_of_args):
            #self.grades += [std_cwid, course, ltr_grade, ins_cwid]
            self.students[std_cwid].add_course(course, ltr_grade)
            self.instructors[ins_cwid].add_course(course)

    def students_summary(self):
        """print studtens table"""
        pt = PrettyTable(['cwid', 'Name', 'Completed Courses'])
        for std in self.students.values():
            pt.add_row([std.cwid, std.name, sorted(std.courses.keys())])
        print(pt)
    
    def instructors_summary(self):
        """print instructors table"""
        pt = PrettyTable(['cwid', 'Name', 'Dept', 'Course', 'Students'])
        for ins in self.instructors.values():
            for course in ins.courses.keys():
                pt.add_row([ins.cwid, ins.name, ins.department, course, ins.courses[course]])
        print(pt)
    

class Person:
    """intilize person object"""

    def __init__(self, cwid, name):
        self.cwid = cwid
        self.name = name


class Student(Person):
    """intilize student object"""

    def __init__(self, cwid, name, major):
        """assign values to student object"""
        super().__init__(cwid, name)
        self.major = major
        self.courses = defaultdict(str)

    def add_course(self, course, grade):
        """add course and grade in defaultdicT(str)"""
        self.courses[course] = grade


class Instructor(Person):
    """intilize instrctor object"""

    def __init__(self, cwid, name, department):
        """assign values to instuctor object"""
        super().__init__(cwid, name)
        self.department = department
        self.courses = defaultdict(int)

    def add_course(self, course):
        """add course and increment students number, stored in defaultdict(st)"""
        self.courses[course] += 1


def main():
    """send files to repository to be read"""
    rep = Repository()
    rep.read_students_file('students.txt', 3)
    rep.read_instructors_file('instructors.txt', 3)
    rep.read_grades_file('grades.txt', 4)
    rep.students_summary()
    rep.instructors_summary()

if __name__ == '__main__':
    main()
