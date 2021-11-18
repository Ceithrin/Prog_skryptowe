from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from timetable2 import Timetable2
from break1 import Break
from basicterm import BasicTerm
from action import Action

# term1 = Term(8, 0, Day.WED)
# term2 = Term(11, 15, Day.WED)
# term3 = Term(13, 30, Day.SAT)
# break1 = Break(BasicTerm(9, 30, 5))
# break2 = Break(BasicTerm(11, 5, 10))
# break3 = Break(BasicTerm(12, 45, 5))

# tt2 = Timetable2([break1, break2, break3])
# tt2.skipBreaks = True

# less1 = Lesson(tt2, term1, 'less1', 'less1', 2)
# less2 = Lesson(tt2, term2, 'less2', 'less2', 2)
# less3 = Lesson(tt2, term3, 'less3', 'less3', 2)


# tt2.put(less1)
# tt2.put(less2)
# tt2.put(less3)

# print(tt2)

# tt2.perform(tt2.parse(['t+']))

# print(tt2)

# print(tt2.lesson_dict['09:35-11:05-Środa'])

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
print(timetable2.lesson_dict)
timetable2.perform(timetable2.parse(['t+']))
print(timetable2.lesson_dict['08:00-9:30-Środa'].term)
print(timetable1.lesson_dict['09:35-11:05-Środa'].term)