import re

from day import Day

def monthChange(string):
    string = re.sub("I", "1", string)
    string = re.sub("II", "2", string)
    string = re.sub("III", "3", string)
    string = re.sub("IV", "4", string)
    string = re.sub("V", "5", string)
    string = re.sub("VI", "6", string)
    string = re.sub("VII", "7", string)
    string = re.sub("VIII", "8", string)
    string = re.sub("IX", "9", string)
    string = re.sub("X", "10", string)
    string = re.sub("XI", "11", string)
    string = re.sub("XII", "12", string)
    return string
    

def weekDay(datetab):
    year = datetab[2] #działa dla dat po 1.1.1700
    month = datetab[1]
    day = datetab[0]
    week   = ['Niedziela', 
              'Poniedziałek', 
              'Wtorek', 
              'Środa', 
              'Czwartek',  
              'Piątek', 
              'Sobota']
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return int(dayOfWeek), week[int(dayOfWeek)]



def dateMatch(string):
    string = monthChange(string)
    date = re.search("(^[0-9]{2})\s([0-9]+)\s([0-9]{4})\s([0-9]+):([0-9]{2})\s-\s([0-9]{2})\s([0-9]+)\s([0-9]{4})\s([0-9]+):([0-9]{2})", string)
    dayS = date.group(1)
    monthS = date.group(2)
    yearS = date.group(3)
    hourS = date.group(4)
    minuteS = date.group(5)
    dayE = date.group(6)
    monthE = date.group(7)
    yearE = date.group(8)
    hourE = date.group(9)
    minuteE = date.group(10)
    datetab = [dayS, monthS, yearS, hourS, minuteS, dayE, monthE, yearE, hourE, minuteE]
    return list(map(int, datetab))

print(dateMatch("27 X 2021 8:00 - 27 X 2021 9:20"))
day = weekDay(dateMatch("27 X 2021 8:00 - 27 X 2021 9:20"))
print(day)



