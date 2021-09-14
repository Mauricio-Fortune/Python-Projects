# Mauricio Fortune Panizo
# COP2930
# Part B: Closing
# 11/6/2020

#Function running to see the latest time they will stay.
def timeToWait(voteTimes,numBooths):
    
    #Initial values given to variables.
    j = 0
    times = []

    #If the values the initial number is increasing by is less than the total booth.
    while j < numBooths:
        
        #Set the total equal to zero.
        boothTime = 0
        
        #Run from the initial values to the amount of numbers and also skipping by the value of booths.
        for i in range (0 + j, len(voteTimes), numBooths):
            
            #Add all the values from one booth together. 
            boothTime += voteTimes [i]

        #Add one to the initial value spot.
        j += 1

        #add the sum from each "for" loop into a list.
        times.append(boothTime)

    #Find the max time from the list.
    total = max(times)

    #Return the max value.
    return total
        

def main():
    #Test Cases
    voteTimes = [3, 8, 2, 9, 6, 5, 12, 3, 4, 4, 8, 9, 7]
    numBooths = 5
    print(timeToWait(voteTimes,numBooths))

    
    voteTimes = [4, 7, 6, 8, 2, 2, 4, 3, 7, 9]
    numBooths = 4
    print(timeToWait(voteTimes,numBooths))

    voteTimes = [5, 9, 7, 4, 4, 8, 2, 5, 6, 8, 11, 16, 2, 3, 1, 4, 6, 7]
    numBooths = 7
    print(timeToWait(voteTimes,numBooths))

    voteTimes = [4, 6, 1, 8, 3, 4, 2, 2, 3]
    numBooths = 10
    print(timeToWait(voteTimes,numBooths))

    voteTimes = [12, 14, 18, 22, 16, 6, 19, 3, 3, 8, 17, 1, 8, 5]
    numBooths = 3
    print(timeToWait(voteTimes,numBooths))

    voteTimes = [15, 7, 9, 2, 4, 2, 5, 5, 10, 12, 4, 17, 16]
    numBooths = 6
    print(timeToWait(voteTimes,numBooths))
    
main ()
