# Mauricio Fortune
# COP2930
# quarantine
# 11/13/2020


# Pre-conditions: seatchart is a list of lists. Each individual list is a list
#                 of strings and all strings are unique. Each string represents
#                 a name and will have one uppercase letter followed by 1 or more
#                 lowercase letters. person will also be a string that follows
#                 the same rules and may or may not appear in seatchart.
# Post-condition: if person is not in seatchart, an empty list is returned. If
#                 person is in seatchart, a list of each name adjacent to person
#                 in seatchart is returned.
def getQuarantineList(seatchart, person):
    quarantined = []
    for i in range(len(seatchart)):
        for j in range(len(seatchart[i])):
            if person == seatchart [i][j]:
                #Above
                if i-1 >= 0:
                    quarantined.append(seatchart[i-1][j])
                #Below
                if i + 1 < len(seatchart):
                    quarantined.append(seatchart[i+1][j])
                #Left
                if j - 1 >= 0:
                    quarantined.append(seatchart[i][j-1])
                #Right
                if j + 1 < len(seatchart[i]):
                    quarantined.append(seatchart[i][j+1])
    return quarantined
                

# This runs a lot of tests.
def test():

    # A regular looking classroom, more than 2 rows and 2 columns.
    scienceClass = [["Anya", "Jane", "Mick", "Lauren"],
                ["Jamil", "Prince", "Janie", "Talia"],
                ["George", "Madison", "Connor", "Jade"]]

    # First test corners.
    print(getQuarantineList(scienceClass, "Anya"))
    print(getQuarantineList(scienceClass, "Lauren"))
    print(getQuarantineList(scienceClass, "George"))
    print(getQuarantineList(scienceClass, "Jade"))

    # Next test borders.
    print(getQuarantineList(scienceClass, "Jane"))
    print(getQuarantineList(scienceClass, "Jamil"))
    print(getQuarantineList(scienceClass, "Connor"))
    print(getQuarantineList(scienceClass, "Talia"))

    # Now test inside and someone not in the class.
    print(getQuarantineList(scienceClass, "Janie"))
    print(getQuarantineList(scienceClass, "Prince"))
    print(getQuarantineList(scienceClass, "James"))

    # This case is usually tricky!
    smallClass = [["Joe"]]
    print(getQuarantineList(smallClass, "Joe"))
    print(getQuarantineList(smallClass, "NotJoe"))

    # Next the one row class.
    atfrontClass = [["Alia","Ben","Cynthia","Darnay","Evelyn"]]
    print(getQuarantineList(atfrontClass, "Alia"))
    print(getQuarantineList(atfrontClass, "Darnay"))
    print(getQuarantineList(atfrontClass, "Evelyn"))
    print(getQuarantineList(atfrontClass, "Flynn"))

    # Lastly, one column
    onecolClass = [["Alia"],["Ben"],["Cynthia"],["Darnay"],["Evelyn"]]
    print(getQuarantineList(onecolClass, "Alia"))
    print(getQuarantineList(onecolClass, "Darnay"))
    print(getQuarantineList(onecolClass, "Evelyn"))
    print(getQuarantineList(onecolClass, "Flynn"))

# Run it!
test()
