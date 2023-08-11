'''
This is a multiline comment...comments are ignored by the interpreter

ASTRONOMY QUIZ TEXT GAME program...covering the most crucial introductory python concepts
AUTHOR(S): krenes neville
	   brianokdev@gmail.com / briankabonyo.netlify.app
'''

#This is a single line comment

import time #importing the time module to use it's functions

def main(): #program entry point...not a must in python but a best practice
	print() #forces a new line

	play = input("Would you like to play a game(yes or no)?").lower()

	#Function to check if player decides to play
	def check_play_choice():
		if play != "yes":
			if play == " ": #nested if statement
				print("ERROR! Entry can't be EMPTY. EXITING in 3 secs...")
				printing("exiting...")
				time.sleep(3) #sleep/pause for 3 seconds
				exit() #quit program
			print("OK. GOODBYE!")
			print("exiting...")
			time.sleep(2)
			exit()
	check_play_choice()

	'''
	Game continues
	'''
	#initialize score and question number variables
	ques_no = 0
	score = 0

	ques_no = ques_no + 1
	print()
	ques = input(f"{ques_no}. Are there billions or millions of stars in our galaxy?").lower()
	if ques == "billions":
		score += 1
		print("CORRECT!")
		print("Congratulations! You earned 1 point.")
	else:
		print("INCORRECT!")
		#print("Answer:{}".format(ques))
		print("Answer: Billions")

	ques_no = ques_no + 1
	print()
	ques = input(f"{ques_no}. What is the most popular unit for measuring interstellar distances?").lower()
	if ques == "light year":
		score += 1
		print("CORRECT!")
		print("Congratulations. You earned 1 point.")
	else:
		print("INCORRECT!")
		print("ANSWER: light year")


	ques_no += 1
	print()
	ques = input(f"{ques_no}. What's the name of our galaxy(HINT: Include spaces)?").lower()
	if ques == "milky way":
		score = score + 1
		print("CORRECT!")
		print("Congratulations! You earned 1 point.")
	else:
		print("INCORRECT!")
		print("ANSWER: milky way galaxy")

	ques_no = ques_no + 1
	print()
	ques = input(f"{ques_no}. What's our closest star system?").lower()
	if ques == "alpha centauri":
		score += 1
		print("CORRECT!")
		print("Congratulations. You earned 1 point.")
	else:
		print("INCORRECT!")
		print("ANSWER: alpha centauri")

	ques_no += 1
	print()

	#List
	local_group = [" andromeda", " milky way", " sombrero", " large magellanic cloud", " triangulum", " small magellanic cloud"]
	
	#Loop
	for item in local_group:
		print(item)

	print()
	ques = input(f"{ques_no}. Which of the above galaxies is not a part of the local group of galaxies?").lower()
	if ques == "sombrero":
		score += 1
		print("CORRECT!")
		print("Congratulations. You earned 1 point.")
		print()
	else:
		print("INCORRECT!")
		print("ANSWER: sombrero")


	ques = input(f"{ques_no}. What object is at the center of most galaxies?").lower()
	if ques == "supermassive black hole":
		score +=1
		print("CORRECT!")
		print("Congratulations. You earned 1 point.")
	else:
		print("INCORRECT!")
		print("ANSWER: supermassive black hole")


	ques_no += 1
	print()
	ques = float(input(f"{ques_no}. How many light years away is alpha centauri?"))
	if ques == 4.37:
		score += 1
		print("CORRECT!")
		print("Congratulations. You earned 1 point.")
	else:
		print("INCORRECT!")
		print("ANSWER: 4.37")


	if score == 0:
		print()
		print("SORRY! You didn't earn any point. Try again!")
	elif score >= 3 and score < 7 : #else if
		print()
		print("GOOD EFFORT! You earned {}/7 points.Try again!".format(score))
	elif score == 7:
		time.sleep(3)
		print()
		print("CONGRATULATIONS! You earned a PERFECT SCORE of {}/7".format(score))
	print()
	print("-------------GAME OVER-------------")
	print("GOODBYE.")
	print("exiting in 5 secs...")
	time.sleep(5)
	exit()


if __name__ == "__main__": #useful to prevent unwanted code execution during a module import
	main()



