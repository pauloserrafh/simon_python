import random
import time

def sort_key(value):
	if (value == 1):
		return 'w'
	if (value == 2):
		return 'a'
	if (value == 3):
		return 's'
	if (value == 4):
		return 'd'


if __name__ == '__main__':
	pressed = 'a'
	blinks = 1
	to_press = []
	finish = False

	while(pressed != 'q' and pressed != 'Q'):
		pressed = input("q or Q to start! ")

	print("q or Q to end game!")

	while(finish == False):
		print("=====================================================================")
		for i in range(blinks):
			to_press.append(sort_key(random.randint(1,4)))
			print(to_press[i], end='\r')
			time.sleep(0.5)
			print(' ', end = '\r')
			time.sleep(0.2)
		j = 0
		for i in range(blinks):
			pressed = input("Press next button: ")
			if (pressed != to_press[j] or pressed == 'q' or pressed == 'Q'):
				finish = True
				print("Game Over")
				print("=====================================================================")
				break
			else:
				j += 1
		else:
			print('Next stage')
		to_press = []
		blinks += 1
