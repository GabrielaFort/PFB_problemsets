#!/usr/bin/env python3
import sys

#This script addresses questions 2 and 3 from the Python 1 problem set


name = sys.argv[1] #Setting up four different arguments for this script - will need to type them in this order
fav_color = sys.argv[2]
fav_activity = sys.argv[3]
fav_animal = sys.argv[4]

print("This script takes four inputs - your name, your favorite color, your favorite activity, and your favorite animal")

if len(sys.argv) > 5:
	print("ERROR: Include only four arguments - name, fav color, fav activity, and fav animal")
	exit()


print(f"My name is:{name}\nMy favorite color is:{fav_color}\nMy favorite activity is:{fav_activity}\nMy favorite animal is:{fav_animal}")

