from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1

term1 = Term(8, 0, Day.WED)
term2 = Term(11, 30, Day.WED)
term3 = Term(13, 30, Day.SAT)

tt1 = Timetable1()

less1 = Lesson(tt1, term1, 'less1', 'less1', 2)
less2 = Lesson(tt1, term2, 'less2', 'less2', 2)
less3 = Lesson(tt1, term3, 'less3', 'less3', 2)


tt1.put(less1)
tt1.put(less2)
tt1.put(less3)

print(tt1)

tt1.perform(tt1.parse(['t-', 'd-', 't+', 'd-']))

print(tt1)