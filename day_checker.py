import sys
date = int(input("Enter a Date: "))
month = input("Enter a month: ").lower()
year = input("Enter a year: ")


a = year[2:]
b = int(a) // 4
c = 0

# YEAR CODE

if 1700 <= int(year) < 1800:
    c = 4
elif 1800 <= int(year) < 1900:
    c = 2
elif 1900 <= int(year) < 2000:
    c = 0
elif 2000 <= int(year) < 2100:
    c = 6
elif 2100 <= int(year) < 2200:
    c = 4
elif 2200 <= int(year) < 2300:
    c = 2
elif int(year) >= 2300:
    c = 0

# MONTH CODE
d = 0
if month == 'january':
    d = 0
elif month == 'february':
    d = 3
elif month == 'march':
    d = 3
elif month == 'april':
    d = 6
elif month == 'may':
    d = 1
elif month == 'june':
    d = 4
elif month == 'july':
    d = 6
elif month == 'august':
    d = 2
elif month == 'september':
    d = 5
elif month == 'october':
    d = 0
elif month == 'november':
    d = 3
elif month == 'december':
    d = 5

# did you mean should add or not??
# LEAP YEAR CONDITION ADD TO IT !!!

# adding all variables
add = int(a) + int(b) + int(c) + int(d) + int(date)

rem = add % 7
# DAY CODE
#Leap Year condition
if date == 29 and month == 'february':
    if int(year) % 4 ==0:
        if int(year) % 100==0:
            if int(year) % 400==0:
                rem-= 1
        else:
            rem-=1
    else:
        print("Invalid Date")
        sys.exit()
        

if rem == 0:
    print("DAY is SUNDAY")
elif rem == 1:
    print("DAY is MONDAY")
elif rem == 2:
    print("DAY is TUESDAY")
elif rem == 3:
    print("DAY is WEDNESDAY")
elif rem == 4:
    print("DAY is THURSDAY")
elif rem == 5:
    print("DAY is FRIDAY")
elif rem == 6:
    print("DAY is SATURDAY")


