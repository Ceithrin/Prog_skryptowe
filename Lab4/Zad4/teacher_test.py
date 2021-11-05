import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from action import Action
from teacher import Teacher


class Test_TestTeacher(unittest.TestCase):


    def test_put1(self):
        timetab = Timetable1()
        teacher1 = Teacher("Ada", "Nowak")
        lesson1 = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", 2, teacher1)
        lesson2 = Lesson(timetab, Term(9, 35, Day.WED), "Prog", 2, teacher1)
        timetab.put(lesson1)
        timetab.put(lesson2)
        self.assertEqual(teacher1.hours, 4)

    def test_add(self):
        term1 = Term(8, 0, Day.WED)
        teacher = Teacher("Ada", "Nowak")
        tt1 = Timetable1()
        less1 = Lesson(tt1, term1, 'less1',  2)

        less1 += teacher
        self.assertEqual(less1._Lesson__teacher, teacher)

    def test_sub(self):
        term1 = Term(8, 0, Day.WED)
        teacher = Teacher("Ada", "Nowak")
        tt1 = Timetable1()
        less1 = Lesson(tt1, term1, 'less1',  2, teacher)

        less1 -= teacher
        self.assertEqual(less1._Lesson__teacher, None)

    def test_sub_add_another(self):
        term1 = Term(8, 0, Day.WED)
        teacher = Teacher("Ada", "Nowak")
        teacher1 = Teacher("Stanisław", "Polak")
        tt1 = Timetable1()
        less1 = Lesson(tt1, term1, 'less1',  2, teacher)
        less1 -= teacher
        less1 += teacher1
        self.assertEqual(less1._Lesson__teacher, teacher1)

    def test_add_to_existing(self):
        term1 = Term(8, 0, Day.WED)
        teacher = Teacher("Ada", "Nowak")
        teacher1 = Teacher("Stanisław", "Polak")
        tt1 = Timetable1()
        less1 = Lesson(tt1, term1, 'less1',  2, teacher)
        less1 += teacher1
        self.assertEqual(less1._Lesson__teacher, teacher)

    def test_to_much_hours(self):
        term1 = Term(8, 0, Day.WED, 270)
        term2 = Term(9, 30, Day.THU)
        teacher = Teacher("Ada", "Nowak")
        teacher1 = Teacher("Stanisław", "Polak")
        tt1 = Timetable1()
        less1 = Lesson(tt1, term1, 'less1',  2, teacher)
        less2 = Lesson(tt1, term2, 'less1',  2, teacher)
        tt1.put(less1)
        self.assertEqual(tt1.put(less2), False)

    




if __name__ == '__main__':
    unittest.main()