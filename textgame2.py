'''
TEXT GAME...involving more python concepts
'''
import time
from check_play_module import check_play_choice

#checks if player decides to play
print()
play = input("Would you like to play a game?").lower()
check_play_choice(play)

'''
Game continues
'''
#initialize score and question variables
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
	print()
	print("Congratulations. You earned 1 point.")
else:
	print("INCORRECT!")
	print("ANSWER: alpha centauri")

ques_no += 1
print()
ques = float(input(f"{ques_no}. How many light years away is it?"))
if ques == 4.37:
	score += 1
	print("CORRECT!")
	print("Congratulations. You earned 1 point.")
else:
	print("INCORRECT!")
	print("ANSWER: 4.37")

if score == 0:
	print("SORRY! You didn't earn any point. Try again.")
elif score >= 3 and score < 5 :
	print("GOOD EFFORT! You earned {}/5 points.Try again".format(score))
elif score == 5:
	time.sleep(3)
	print("CONGRATULATIONS! You have earned a PERFECT SCORE of {}/5".format(score))
print()
print("-------------GAME OVER-------------")
print("GOODBYE.")
print("exiting in 5 secs...")
time.sleep(5)
exit()





