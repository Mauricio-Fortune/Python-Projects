# Mauricio Fortune Panizo
# COP2930
# Groundhog Month Calendar
# 10/3/2020


#Find the number of months
month = int(input("How many months are there on the Groundhog calendar?\n"))

#Find the number of days in each month
days = int(input("How many days per month are there on the groundhog calendar?\n"))

#Calculate the amount of rows
rows = days//7

#For statement in the range 1 to the chosen month
for i in range (1, month + 1):
    print()

    #Set the first day to zero
    weekday = 0

    #Print which month it is
    print("Month",i)

    #Print the days of the week
    print("S\tM\tT\tW\tR\tF\tS")

    #Set the rows starting from one to the amount of rows
    for row in range (1, rows + 1):

        #Set the columns to go to exactly 7 days each week
        for col in range (1, 8):

            #Continually add one to each day
            weekday= weekday + 1
            print(weekday, end="\t")
        print()
