#Create a python algorithm that asks for a colour, shape and an integer. 
#The code is in a loop to ask for another colour, shape and an integer. 
#The tally of different shapes, colours, and integers is displayed. 
#Eg red square 2, red triangle 3, blue square 5, blue circle 7. 

exitFlag = False
shapes = {}
colours = {} 
integers = {}
while exitFlag != True:
    userShape = input("What Shape? ")
    if userShape != "exit":
        userColour = input("What colour? ")
        if userShape != "exit":
            userInteger = input("What integer? ")
            if userInteger != "exit":
                userInteger = int(userInteger)

                #add if in dictionary
                if userShape in shapes:
                    shapes[userShape] += 1
                else:
                    shapes[userShape] = 1

                #add if in dictionary
                if userColour in colours:
                    colours[userColour] += 1
                else:
                    colours[userColour] = 1

                if userInteger in integers:
                    integers[userInteger] += 1
                else:
                    integers[userInteger] = 1

            else:
                exitFlag = True
        else:
            exitFlag = True
    else:
        exitFlag = True 

print(shapes)
print(colours)
print(integers)
