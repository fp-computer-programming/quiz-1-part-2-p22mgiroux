# Author: MOG 10/19/21

day = input("Enter the day of the date: ")
month = input("Enter the month of the date: ")
long_year = input("Enter the year of the date: ")

short_year = int(long_year) % 100
century = int(long_year) // 100
if int(month) == 1:
    month = 13
if int(month) == 2:
    month = 14

day_number = (int(day) + ((26 * (int(month) + 1)) // 10) + int(short_year) + (int(short_year) // 4) + (int(century) // 4) + (5 * int(century))) % 7

if day_number == 0:
    day_of_the_week = "Saturday"
if day_number == 1:
    day_of_the_week = "Sunday"
if day_number == 2:
    day_of_the_week = "Monday"
if day_number == 3:
    day_of_the_week = "Tuesday"
if day_number == 4:
    day_of_the_week = "Wednesday"
if day_number == 5:
    day_of_the_week = "Thursday"
if day_number == 6:
    day_of_the_week = "Friday"

print(str(day) + "/" + str(month) + "/" + str(long_year) + " is a " + str(day_of_the_week))