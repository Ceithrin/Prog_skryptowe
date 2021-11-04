import unittest
from day import Day
from term import Term
from lesson import Lesson

class Test_TestDeanerySystem(unittest.TestCase):

    def test_lesson_earlierDay(self):
        self.assertTrue(Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2).earlierDay())
        self.assertFalse(Lesson(Term(9, 35, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2).earlierDay())
        self.assertFalse(Lesson(Term(9, 35, Day.SAT), "Programowanie skryptowe", "Stanisław Polak", 2).earlierDay())
        self.assertTrue(Lesson(Term(9, 35, Day.SUN), "Programowanie skryptowe", "Stanisław Polak", 2).earlierDay())

    def test_lesson_laterDay(self):
        self.assertTrue(Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2).laterDay())
        self.assertFalse(Lesson(Term(9, 35, Day.SUN), "Programowanie skryptowe", "Stanisław Polak", 2).laterDay())
        self.assertFalse(Lesson(Term(18, 35, Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2).laterDay())
        self.assertFalse(Lesson(Term(9, 35, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2).laterDay())

    def test_lesson_ealierTime(self):
        self.assertTrue(Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2).ealierTime())
        self.assertFalse(Lesson(Term(8, 35, Day.SUN), "Programowanie skryptowe", "Stanisław Polak", 2).ealierTime())
        self.assertFalse(Lesson(Term(17, 35, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2).ealierTime())
        self.assertTrue(Lesson(Term(20, 00, Day.FRI, 120), "Programowanie skryptowe", "Stanisław Polak", 2).ealierTime())

    def test_lesson_laterTime(self):
        self.assertTrue(Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2).laterTime())
        self.assertFalse(Lesson(Term(19, 35, Day.SUN), "Programowanie skryptowe", "Stanisław Polak", 2).laterTime())
        self.assertFalse(Lesson(Term(16, 35, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2).laterTime())
        self.assertTrue(Lesson(Term(17, 00, Day.FRI, 120), "Programowanie skryptowe", "Stanisław Polak", 2).laterTime())



if __name__ == '__main__':
    unittest.main()