# Mauricio Fortune
# COP 2930
# Report
# 11/20/2020


#Create a dictionary and a list 
mydictionary= {}
allResults = []

#Find if they want to upload files or not
run = input("Would you like to upload another file(yes/no)?\n")

#If they say yes and continue to say yes run the following program
while run == 'yes':

    #Get the file name of the file from where they want the data analyzed
    filename = input("What is the name of the file?\n")

    #Open the file with the given file name
    file = open(filename, "r")

    #Get the number at the top of each document
    numTests = int(file.readline())

    #Run this program the amount of times the given number above gives
    for i in range(numTests):

        #Get the name and the results of the people.
        name = file.readline().rstrip()
        covidresults = file.readline().rstrip()

        #If their name is not in the dictionary then add it
        if not name in mydictionary:
            mydictionary[name] = covidresults

        #If their name is in the dictionary, only change their results
        #if the test result was positive
        else:
            #If a prior test was positive then leave it
            if mydictionary[name] == "positive":
                mydictionary[name] = "positive"
            #If a prior test was not positive then you can change it to
            #result of the new test
            if mydictionary[name] != "positive":
                mydictionary[name] = covidresults

    #Tell them the fil was uploaded
    print(filename, "has been uploaded.")

    #Find out if they want to have another file analyzed
    run = input("Would you like to upload another file(yes/no)?\n")
    
#put the names in alaphabetical order
for name in sorted (mydictionary.keys()):

    #Get the alphabetical names and put them into the list
    allResults.append(name+ ' ' +mydictionary[name])

#If they do not want anymore files analyzed
else:
    #Get the name of the file they want to store their analyzed information into
    storeFile = input("Which file would you like the final results stored in?\n")

    #Write into that file
    myFile = open(storeFile, "w")

    #Print that initial number giving the total amount of people
    myFile.write(str(len(allResults)))
    myFile.write("\n")

    #Write out all the names
    for i in range (len(allResults)):
        myFile.write(str(allResults[i]))
        myFile.write("\n")
        
    #Close the file
    myFile.close()

    #Tell them the status of their stored information
    print("Your results have been stored.")
    print("Thank you for using the test data accumulator program!")






        
            
            










   
       











