# Mauricio Fortune Panizo
# COP2930
# Spirograph
# 09/26/2020

import turtle

#Get turtle in the correct position
turtle.penup()
turtle.setpos(-50,-200)
turtle.pendown()

#Set the amount of time this for loop is going to run
for i in range (24):
    
    #Set the range for the turns for the triangle within the for loop
    for triangle in range (3):
        
        #Triangle
        turtle.left(45)
        turtle.forward(400)
        turtle.right(120)
        
        #Set the angle to turn when starting the next triangle
        for angle in range (1):
            turtle.right(170)

    

