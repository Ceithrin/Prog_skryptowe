import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable2 import Timetable2
from action import Action
from break1 import Break
from basicterm import BasicTerm


class Test_TestTimetable2(unittest.TestCase):


    def test_put1(self):
        timetab = Timetable2()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(timetab.put(lesson), True)

    def test_put2(self):
        bl = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        timetable = Timetable2(bl)
        les0 = Lesson(timetable, Term(9, 30, Day.TUE), "-", "-", 2)
        with self.assertRaises(ValueError):
            timetable.put(les0)          

    def test_get_smth(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.get(termin), lesson)

    def test_get_None(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        self.assertEqual(timetab.get(lesson), None)

    def test_busy_same(self):
        timetab = Timetable2()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.busy(lesson.term), True)

    def test_busy_overlap(self):
        timetab = Timetable2()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        termin = Term(9, 5, Day.TUE)
        timetab.put(lesson)
        self.assertEqual(timetab.busy(termin), True)

    def test_busy_not(self):
        timetab = Timetable2()
        lesson = Lesson(timetab, Term(9, 35, Day.TUE), "Prog", "Prog", 2)
        self.assertEqual(timetab.busy(lesson.term), False)

    def test_can_be_transferred_to_full_time_ok(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.TUE)
        termin1 = Term(11, 00, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(termin1, True), True)

    def test_can_be_transferred_to_full_time_false(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.TUE)
        termin1 = Term(11, 00, Day.SAT)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(termin1, True), False)

    def test_can_be_transferred_to_no_full_time_true(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.SAT)
        termin1 = Term(11, 00, Day.SAT)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(termin1, False), True)

    def test_can_be_transferred_to_no_full_time_false(self):
        timetab = Timetable2()
        termin = Term(9, 30, Day.SAT)
        termin1 = Term(11, 00, Day.TUE)
        lesson = Lesson(timetab, termin, "Prog", "Prog", 2)
        timetab.put(lesson)
        self.assertEqual(timetab.can_be_transferred_to(termin1, False), False)

    def test_parse(self):
        timetab = Timetable2()
        strl = ['d-', 'd+', 't-', 't+']
        action_list = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(timetab.parse(strl), action_list)

    def test_parse_exception(self):
        timetab = Timetable2()
        strl = ['d-', 'd+', 't-', 't+', 'dfsbfjkb']
        with self.assertRaises(ValueError):
            timetab.parse(strl)

    def test_peform_skipBreakFalse(self):
        breaks = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        timetable1 = Timetable2(breaks)
        timetable2 = Timetable2(breaks)
        termin1 = Term(8, 0, Day.WED)
        lesson1 = Lesson(timetable2, termin1, 'lekcja', 'Stanisław Polak', 2)
        action_list = [Action.TIME_LATER]
        timetable1.put(lesson1)
        timetable2.skipBreaks = False
        timetable2.put(lesson1) 
        timetable2.perform(action_list) #nie wykona sie bo pokrywa sie z przerwa
        self.assertEqual(timetable2.lesson_dict, timetable1.lesson_dict)

    def test_peform_skipBreakTrue(self):
        breaks = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        timetable1 = Timetable2(breaks)
        timetable2 = Timetable2(breaks)
        termin1 = Term(8, 0, Day.WED)
        termin2 = Term(9, 35, Day.WED)
        lesson1 = Lesson(timetable2, termin1, 'lekcja', 'Stanisław Polak', 2)
        lesson2 = Lesson(timetable2, termin2, 'lekcja', 'Stanisław Polak', 2)
        action_list = [Action.TIME_LATER]
        timetable1.put(lesson2)
        timetable2.skipBreaks = True
        timetable2.put(lesson1)
        timetable2.perform(action_list)
        self.assertEqual(lesson1.term, lesson2.term)



    


if __name__ == '__main__':
    unittest.main()