# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic

# Driver code
if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = logic.start_game()

print("\nGame Start")
exitFlag = False
while(not exitFlag):
	action = True

	# taking the user input
	# for next step
	x = input("\nPress the command : ")

	# we have to move up
	if(x == 'W' or x == 'w'):

		# call the move_up function
		mat, flag = logic.move_up(mat)

	# the above process will be followed
	# in case of each type of move
	# below

	# to move down
	elif(x == 'S' or x == 's'):
		mat, flag = logic.move_down(mat)

	# to move left
	elif(x == 'A' or x == 'a'):
		mat, flag = logic.move_left(mat)

	# to move right
	elif(x == 'D' or x == 'd'):
		mat, flag = logic.move_right(mat)
	
	elif(x.lower() == 'exit'):
		action = False
		exitFlag = True

	#neither of the above
	else:
		print("Invalid Key Pressed")
		action = False

	if action:	
		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		#if there is a gameover, exit.
		if (logic.gameOver(status, mat) == True):
			exitFlag = True
	# print the matrix after each move.
	logic.displayMat(mat)

print("\nGame End")