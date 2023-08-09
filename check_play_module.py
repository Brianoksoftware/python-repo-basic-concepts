'''
check play choice function
'''
import time

def check_play_choice(play):
	if play != "yes":
		if play == " ":
			print("ERROR! Entry can't be EMPTY. EXITING in 3 secs...")
			printing("exiting...")
			time.sleep(3)
			exit()
		print("OK. GOODBYE!")
		print("exiting...")
		time.sleep(2)
		exit()