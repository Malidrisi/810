# -*- coding: utf-8 -*-
#Homework09_Test - Author Maha

import unittest
from HW09_Maha import Repository
from HW09_Maha import Student
from HW09_Maha import Instructor

class HW09Test(unittest.TestCase):
    """Test the Student class """
    s_1 = Student('1122', 'Maha A.', 'SE')
    s_1.add_course('SSW810', 'A')
    i_1 = Instructor('1212', 'Jim', 'SE')
    i_1.add_course('SSW810')

    def test_studnet_init(self):
        """tests student initlization"""
        self.assertEqual((HW09Test.s_1.cwid, HW09Test.s_1.name, HW09Test.s_1.major), ('1122', 'Maha A.', 'SE'))

    def test_stuednt_add_course(self):
        """tests add course function"""
        self.assertEqual(HW09Test.s_1.courses, {'SSW810': 'A'})

    def test_instructor_init(self):
        """tests instructor initlization"""
        self.assertEqual((HW09Test.i_1.cwid, HW09Test.i_1.name, HW09Test.i_1.department), ('1212', 'Jim', 'SE'))

    def test_instructor_add_course(self):
        """tests student initlization"""
        self.assertEqual(HW09Test.i_1.courses, {'SSW810': 1})

    def test_repository(self):
        """test rep class"""
        rep = Repository()
        self.assertEqual((rep.students, rep.instructors), ({}, {}))
        self.assertRaises(FileNotFoundError, rep.read_students_file, 'doesnt_exist.txt', 2)
        self.assertRaises(ValueError, rep.read_students_file, 'students.txt', 2)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
