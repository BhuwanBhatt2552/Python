
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime
from zoneinfo import ZoneInfo

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now(ZoneInfo("Asia/Kolkata"))

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# print(now.strftime("The current year is :%y"))
# print(now.strftime("The current year is :%Y"))
# print(now.strftime("%a, %A, %d, %B, %b "))


# %c - locale's date and time, %x - locale's date, %X - locale's time
# print(now.strftime("local date and time %c"))
# print(now.strftime("local date and time %x"))
# print(now.strftime("local date and time %X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("Current time: %I: %M: %S: %p"))