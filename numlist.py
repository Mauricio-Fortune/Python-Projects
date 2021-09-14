# Mauricio Fortune Panizo
# COP2930
# Problem A: numlist
# October 29,2020



def menu ():

    #Print the available options
    print("What selection would you like to make?")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Print the list")
    print("4. Quit")

    #Get the answer and return it
    ans = int(input(""))
    return ans

def main ():
    
    numbers = []
    
    #Get what they want to do from the list
    ans = menu()

    while ans < 4:
    
        #If they pick 1
        if ans == 1:
            newnum = int(input("What number would you like to add?\n"))
            numbers.append(newnum)
            print("Your number has been added.\n")

        #If they pick 2
        elif ans == 2:
            removeNum = int(input("What number would you like to remove?\n"))
            #If the number is removable
            if removeNum in numbers:
                numbers.remove(removeNum)
                print("Your number has been removed.\n")
            #If the number is not in the list
            else:
                print("Sorry, that number is not in the list.\n")

        #If they pick 3
        elif ans == 3:
            print("Your list is", numbers,"\n")
        #Reprint the menu
        ans = menu()  
        
    #If they pick 4, end it and print
    print("Thank you for using the list generator!")

main()
        
