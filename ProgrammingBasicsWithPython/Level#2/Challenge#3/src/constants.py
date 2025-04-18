# Created by Mahros


# TESTED SUCCESSFULLY
# This is constants file that will store all constatns!


# Dependencies
import src.calc_module as cam
import math
import random


# make custom sqrt
def sqrt(a:int, b):
	return math.sqrt(a)

def rand(a:float, b:float):
	return random.randint(int(a), int(b))
# operators
oprs = {
	# 4
	"add":(cam.add, ["+", "add", "sum"]),
	"sub":(cam.sub, ["-", "sub"]),
	"div":(cam.div, ["/", "div"]),
	"mut":(cam.mlt, ["*", "mut"]),

	# 6
	"rot":(sqrt, ["rot"]),
	"exp":(math.exp, 	["exp", "pow"]),

	# 7
	"rnd":(rand, ["rnd", "rand", "random"]),
}
