import math as m
import timeit
start = timeit.default_timer()

class Year:
    def __init__(self, name, first_day) :
        self.name = str(name)
        self.annum = int(name)
        self.first_day = first_day
        if ((self.annum % 400 == 0) or ((self.annum % 4 == 0) and not(self.annum % 100 == 0))) :
            days = 366
            firsts = [1,32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
        else :
            days = 365
            firsts = [1,32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        self.days = days
        self.firsts = firsts
        first_of_months =[]
        i = 0
        first_Sundays = 0
        while i < len(firsts) :
            first_day_of_month = ((first_day + firsts[i] -1)% 7)
            first_of_months.append(first_day_of_month)
            if first_day_of_month == 0:
                first_Sundays +=1
            i += 1
        self.first_of_months = first_of_months
        self.first_Sundays = first_Sundays
        last_day = (first_day + days - 1) % 7
        self.last_day = last_day
        

Year_zero = Year(1900, 1)

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

firsts_on_Sundays = 0
Years = []
Years.insert(0,Year_zero)
i = 1
while i <= 100 :
    start_day = (Years[(i-1)].last_day + 1) % 7
    annum = Year_zero.annum + i
    new_year = Year(annum, start_day)
    firsts_on_Sundays += new_year.first_Sundays
    Years.insert(i,new_year)
    i += 1

i = 0
while i < len(Years) :
    print(Years[i].name + " starts on a " + days_of_the_week[Years[i].first_day] + " and ends on a " + days_of_the_week[Years[i].last_day] + ".  It had " + str(Years[i].first_Sundays) + " months that started on a Sunday.")
    i += 1

print("There were ", firsts_on_Sundays, "in the twentieth century.")

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")