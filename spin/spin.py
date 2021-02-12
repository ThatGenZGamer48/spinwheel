import random
import time

class spin:
	def start_spin():
		print('''
			-- Welcome to the Spinwheel Game --
			You will be asked to enter five choices
			and this program will spin the wheel and
			pick a random choice from the choices
			you gave!! 
			''')
		first_choice = input("Enter first choice: ")
		second_choice = input("Enter second choice: ")
		third_choice = input("Enter third choice: ")
		four_choice = input("Enter four choice: ")
		fifth_choice = input("Enter fifth choice: ")
		choices = [str(first_choice),
				   str(second_choice),
				   str(third_choice),
				   str(four_choice),
				   str(fifth_choice)]
		print('Validating choices!')
		time.sleep(1)
		print('Spinning wheel!')
		time.sleep(2)
		print('You have got, {} as your option'.format(random.choice(choices)))
		print('Thank you for playing!')
