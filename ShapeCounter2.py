#The user is asked if they would like to change any of the details and this is displayed as 
#“There were N COLOURED SHAPE and it has been updated to N2 COLOURED SHAPE” for each different colour 
#and / or shape. 
#If there is a shape or colour dissimilar to the original round, 
#this must also be displayed “The original shape was SHAPE and it was updated to SHAPE.” 
#Repeat this for colour.

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

                integer = userInteger
                colour = userColour
                shape = userShape

                #Add to Dicionaries
                #add if in dictionary
                if userShape in shapes:
                    shapes[userShape] += 1
                else:
                    shapes[userShape] = 1
                    dissimilar = True

                #add if in dictionary
                if userColour in colours:
                    colours[userColour] += 1
                else:
                    colours[userColour] = 1
                    dissimilar = True

                if userInteger in integers:
                    integers[userInteger] += 1
                else:
                    integers[userInteger] = 1
                    dissimilar = True
                
                if dissimilar:
                    print("\n--------------------------------------------------------------------")
                    print(f"The original shape was {shape} and it was updated to {userShape}")
                    print(f"The original colour was {colour} and it was updated to {userColour}")
                    print(f"The original shape was {integer} and it was updated to {userInteger}")
                    print("-------------------------------------------------------'exit'-to-exit\n")

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