import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from teacher import Teacher

class Test_TestLesson(unittest.TestCase):

    def test_earlierDay_fullTime1(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(11, 30, Day.WED), "Prog", 2, Teacher("Stanisław", "Polak"))
        self.assertTrue(lesson.earlierDay())
    





if __name__ == '__main__':
    unittest.main()