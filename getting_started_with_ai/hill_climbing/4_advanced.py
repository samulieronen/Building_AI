import math
import random

def main():

	prob = 0.80
	if random.random() < prob:
		favourite = "dogs"  # change this
		print("I love " + favourite)
	else:
		prob = 0.5
		if random.random() < prob:
			favourite = "cats"  # change this
			print("I love " + favourite)
		else:
			favourite = "bats"  # change this
			print("I love " + favourite)

main()
