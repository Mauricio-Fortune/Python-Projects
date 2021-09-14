# Mauricio Fortune Panizo
# COP 2930
# Sales Commission
# 09/09/2020

#Find out how many hours they worked
hours = int(input("How many hours did you work this week?\n"))

#find out how many slaes they made
sales = int(input("How many sales did you make this week?\n"))

#How much money they made off hours worked
hourlypay = hours*8

#Calculate total money and sales made
#Sales less than or equal to 10 a week
if sales <= 10:
    salesunderten = sales * 5
    total = hourlypay + salesunderten
#Sales greater than 10 a week
else:
    firsttensales = 50
    salesoverten = sales - 10
    totaloverten = salesoverten * 15
    totalsales = totaloverten + firsttensales
    total = hourlypay + totalsales

#Total printed out
print("You made",total,"dollars this week!")
