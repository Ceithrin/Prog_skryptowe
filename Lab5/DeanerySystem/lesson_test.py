import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1

class Test_TestLesson(unittest.TestCase):

    def test_earlierDay_fullTime1(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(11, 30, Day.WED), "Prog", "Prog", 2)
        self.assertTrue(lesson.earlierDay())

    def test_earlierDay_fullTime2(self):
        timetab = Timetable1()
        lesson1 = Lesson(timetab, Term(9, 35, Day.MON), "Prog", "Prog", 2)
        self.assertFalse(lesson1.earlierDay())

    def test_earlierDay_noFullTime1(self):
        timetab = Timetable1()
        lesson2 = Lesson(timetab, Term(12, 35, Day.SUN), "Prog", "Prog", 2)
        self.assertTrue(lesson2.earlierDay())

    def test_earlierDay_noFullTime2(self):
        timetab = Timetable1()
        lesson3 = Lesson(timetab, Term(8, 30, Day.SAT), "Prog", "Prog", 2)
        self.assertFalse(lesson3.earlierDay())
    
    def test_laterDay_ft_true(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(lesson.laterDay(), True)

    def test_laterDay_ft_false(self):
        timetab = Timetable1()
        lesson1 = Lesson(timetab, Term(17, 35, Day.THU), "Prog", "Prog", 2)
        self.assertEqual(lesson1.laterDay(), False)

    def test_laterDay_nft_true(self):
        timetab = Timetable1()
        lesson2 = Lesson(timetab, Term(14, 35, Day.SAT), "Prog", "Prog", 2)
        self.assertEqual(lesson2.laterDay(), True)

    def test_laterDay_nft_false(self):
        timetab = Timetable1()
        lesson3 = Lesson(timetab, Term(9, 35, Day.SUN), "Prog", "Prog", 2)
        self.assertEqual(lesson3.laterDay(), False)


    def test_earlierTime_ft_true(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(lesson.earlierTime(), True)

    def test_earlierTime_ft_false(self):
        timetab = Timetable1()
        lesson1 = Lesson(timetab, Term(8, 5, Day.MON), "Prog", "Prog", 2)
        self.assertEqual(lesson1.earlierTime(), False)

    def test_earlierTime_nft_true(self):
        timetab = Timetable1()
        lesson2 = Lesson(timetab, Term(17, 35, Day.SAT), "Prog", "Prog", 2)
        self.assertEqual(lesson2.earlierTime(), True)

    def test_earlierTime_nft_false(self):
        timetab = Timetable1()
        lesson3 = Lesson(timetab, Term(17, 35, Day.FRI), "Prog", "Prog", 2)
        self.assertEqual(lesson3.earlierTime(), False)
    

    def test_laterTime_ft_true(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(lesson.laterTime(), True)

    def test_laterTime_ft_false(self):
        timetab = Timetable1()
        lesson1 = Lesson(timetab, Term(17, 35, Day.THU), "Prog", "Prog", 2)
        self.assertEqual(lesson1.laterTime(), False)

    def test_laterTime_nft_true(self):
        timetab = Timetable1()
        lesson2 = Lesson(timetab, Term(14, 35, Day.SAT), "Prog", "Prog", 2)
        self.assertEqual(lesson2.laterTime(), True)

    def test_laterTime_nft_false(self):
        timetab = Timetable1()
        lesson3 = Lesson(timetab, Term(17, 35, Day.SUN), "Prog", "Prog", 2)
        self.assertEqual(lesson3.laterTime(), False)






if __name__ == '__main__':
    unittest.main()