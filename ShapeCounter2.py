#The user is asked if they would like to change any of the details and this is displayed as 
#“There were N COLOURED SHAPE and it has been updated to N2 COLOURED SHAPE” for each different colour 
#and / or shape. 
#If there is a shape or colour dissimilar to the original round, 
#this must also be displayed “The original shape was SHAPE and it was updated to SHAPE.” 
#Repeat this for colour.

def tallyToDict(value, dict):
    if value in dict:
        dict[value] += 1
        return False
    else:
        dict[value] = 1
        return True


exitFlag = False
integer = 0
colour = "N/A"
shape = "N/A"

#The dictionaries
shapes = {}
colours = {} 
integers = {}

while exitFlag != True:
    userShape = input("What Shape? ")
    if userShape.lower() != "exit":
        userColour = input("What colour? ")
        if userShape.lower() != "exit":
            userInteger = input("What integer? ")
            if userInteger.lower() != "exit":
                userInteger = int(userInteger)

                dissimilar = False


                #Add to Dicionaries
                dissimilar = tallyToDict(userShape, shapes)
                dissimilar = tallyToDict(userColour, colours)
                dissimilar = tallyToDict(userInteger, integers)
                if dissimilar:
                    print("\n--------------------------------------------------------------------")
                    print(f"The original shape was {shape} and it was updated to {userShape}")
                    print(f"The original colour was {colour} and it was updated to {userColour}")
                    print(f"The original shape was {integer} and it was updated to {userInteger}")
                    print("-------------------------------------------------------'exit'-to-exit\n")
                else:
                    print("\nNothing Different----------------------------------------------------\n") 
                integer = userInteger
                colour = userColour
                shape = userShape

            else:
                exitFlag = True
        else:
            exitFlag = True
    else:
        exitFlag = True 

print(f"Shapes: {shapes}")
print(f"Colours: {colours}")
print(f"Integers: {integers}")
print("Finished")