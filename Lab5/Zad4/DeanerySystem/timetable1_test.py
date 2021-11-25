import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from action import Action


class Test_TestTimetable(unittest.TestCase):


    def test_put1(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(timetab.put(lesson), True)

    def test_put2(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        lesson1 = Lesson(timetab, Term(8, 35, Day.TUE), "Prog", "Prog", 2)
        timetab.put(lesson)
        with self.assertRaises(ValueError):
            timetab.put(lesson1)  

    def test_get_smth(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.get(termin), lesson)

    def test_get_None(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        self.assertEqual(timetab.get(lesson), None)

    def test_busy_same(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.busy(lesson.term), True)

    def test_busy_overlap(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        termin = Term(9, 5, Day.TUE)
        timetab.put(lesson)
        self.assertEqual(timetab.busy(termin), True)

    def test_busy_not(self):
        timetab = Timetable1()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(timetab.busy(lesson.term), False)

    def test_can_be_transferred_to_full_time_ok(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(ter1, True), True)

    def test_can_be_transferred_to_full_time_false(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.SAT)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(ter1, True), False)

    def test_can_be_transferred_to_no_full_time_true(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.SAT)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(ter1, False), True)

    def test_can_be_transferred_to_no_full_time_false(self):
        timetab = Timetable1()
        termin = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(ter1, False), False)

    def test_parse(self):
        timetab = Timetable1()
        strl = ['d-', 'd+', 't-', 't+']
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(timetab.parse(strl), actl)



if __name__ == '__main__':
    unittest.main()