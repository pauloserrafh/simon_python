import random
import time
import RPi.GPIO as GPIO

# buttons
start_button = 5
green_button = 6
red_button = 13
yellow_button = 19
blue_button = 26

# LEDs
green_led = 25
red_led = 8
yellow_led = 7
blue_led = 1

def read_button():
	while (not (GPIO.input(green_button) or GPIO.input(red_button) or GPIO.input(yellow_button) or GPIO.input(blue_button))):
		pass
	if GPIO.input(green_button):
		return 1
	if GPIO.input(red_button):
		return 2
	if GPIO.input(yellow_button):
		return 3
	if GPIO.input(blue_button):
		return 4

def leds_off():
	GPIO.output(green_led, GPIO.LOW)
	GPIO.output(red_led, GPIO.LOW)
	GPIO.output(yellow_led, GPIO.LOW)
	GPIO.output(blue_led, GPIO.LOW)

def sort_led(value):
	if (value == 1):
		GPIO.output(green_led, GPIO.HIGH)
		return value
	if (value == 2):
		GPIO.output(red_led, GPIO.HIGH)
		return value
	if (value == 3):
		GPIO.output(yellow_led, GPIO.HIGH)
		return value
	if (value == 4):
		GPIO.output(blue_led, GPIO.HIGH)
		return value

def blink_game_start():
	for i in range(5):
		GPIO.output(green_led, GPIO.HIGH)
		GPIO.output(red_led, GPIO.HIGH)
		GPIO.output(yellow_led, GPIO.HIGH)
		GPIO.output(blue_led, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(green_led, GPIO.LOW)
		GPIO.output(red_led, GPIO.LOW)
		GPIO.output(yellow_led, GPIO.LOW)
		GPIO.output(blue_led, GPIO.LOW)
		time.sleep(0.2)
	leds_off()
	time.sleep(0.5)

def blink_next_stage():
	leds_off()
	for i in range(5):
		GPIO.output(green_led, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(green_led, GPIO.LOW)

		GPIO.output(red_led, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(red_led, GPIO.LOW)

		GPIO.output(yellow_led, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(yellow_led, GPIO.LOW)

		GPIO.output(blue_led, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(blue_led, GPIO.LOW)
	leds_off()
	time.sleep(0.5)

def setup():
	GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

	# Buttons setup as INPUT with pull-down resistors
	GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	# LEDs setup as OUTPUT
	GPIO.setup(green_led, GPIO.OUT)
	GPIO.setup(red_led, GPIO.OUT)
	GPIO.setup(yellow_led, GPIO.OUT)
	GPIO.setup(blue_led, GPIO.OUT)
	leds_off()

def main():
	setup()
	while(True):
		blinks = 1
		to_press = []
		finish = False
		
		# Waits for start button to be pressed and released
		while(not GPIO.input(start_button)):
			pass

		while(GPIO.input(start_button)):
			pass

		blink_game_start()

		while(finish == False):
			# If the start button is pressed at any time, resets the game
			if(GPIO.input(start_button)):
				finish = True
				blink_game_start()
				break
			for i in range(blinks):
				to_press.append(sort_led(random.randint(1,4)))
				time.sleep(0.5)
				leds_off()
				time.sleep(0.5)
			j = 0
			for i in range(blinks):
				# If the start button is pressed at any time, resets the game
				if(GPIO.input(start_button)):
					finish = True
					blink_game_start()
					break
				pressed = read_button()
				print('to_press:')
				print(to_press)
				print('pressed:')
				print(pressed)

				if (pressed != to_press[j]):
					finish = True
					blink_game_start()
					break
				else:
					j += 1

				while (GPIO.input(green_button) or GPIO.input(red_button) or GPIO.input(yellow_button) or GPIO.input(blue_button)):
					pass
			else:
				blink_next_stage()
			to_press = []
			blinks += 1


if __name__ == '__main__':
	try:
		main()
	except:
		print("Program aborted")
	finally:
		GPIO.cleanup()