# Mauricio Fortune Panizo
# COP2930
# Milesb
# 09/24/2020

#Find out how many days total they want to run.
D = int(input("How many days do you plan to run?\n"))

#Find out how far they want to run during the weekday.
Mweekday= int(input("How many miles per weekday do you plan to run?\n"))

#Find out how far they want to run during the weekend.
Mweekend= int(input("How many miles per weekend day do you plan to run?\n"))

#Set the initial value for total miles.
total = 0

#For loop that goes until the last day.
for D in range (1, D+1):

    #Find out which days are weekends and apply the different values to them.
    if D % 7 == 0 or D % 7 == 6:
        total = total + Mweekend
        print("After day ", D,", you will have completed ", total," miles.", sep="")

    #Add the value they are running during the weekdays to the weekdays.
    else:
        total = total + Mweekday
        print("After day ", D,", you will have completed ", total," miles.", sep="")
