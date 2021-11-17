from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from teacher import Teacher

term1 = Term(8, 0, Day.WED, 150)
term2 = Term(11, 30, Day.WED)
term3 = Term(13, 30, Day.SAT)
teacher = Teacher("Ada", "Nowak")
teacher2 = Teacher("Stanisław", "Polak")

tt1 = Timetable1()

less1 = Lesson(tt1, term1, 'less1',  2, teacher)
less2 = Lesson(tt1, term2, 'less2',  2, teacher)
less4 = Lesson(tt1, term3, 'less4',  2)

less4 += teacher2

tt1.put(less1)
tt1.put(less2)

print(less4)
print(tt1)
print(teacher.hours)