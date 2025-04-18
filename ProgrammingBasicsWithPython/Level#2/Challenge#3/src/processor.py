#
# Created by Mahros
#

# Name: Processor.py
# Desc: Handle any calculation


# Dependencies
import src.calc_module as cam
import src.constants as con

def processor(n1:float, n2:float, opr:str):
	out = 0.0 # this will be the box of the calc. result

	for key in con.oprs:
		if opr in con.oprs[key][1]:
			return con.oprs[key][0](n1, n2)

	return "Invalid operator"


if __name__ == "__main__":
	# Make automated test here
	pass
