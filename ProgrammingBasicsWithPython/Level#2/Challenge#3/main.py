# this is the main file 

# Modules
import src.processor as pro

# now, the program logic here
# Features
# 4-functions for simple calculation with two operands
# user has to enter two numbers, and the 
# 2-functions for roots and exponents
# last function witll give the user random number between n1, and n2



# Handle 
def main():
	print("====== Calculator ======")
	n1 = float(input("n1: "))
	n2 = float(input("n2: "))
	op = input("op: ")

	TYPE = type(0.0)

	if type(n1) is not TYPE:
		print(f"n1 is not number: {n1}")
		return
	if type(n2) is not TYPE:
		print(f"n2 is not number: {n2}")
		return
	result = pro.processor(n1, n2, op)
	fprint = f"Formula> {n1} {op} {n2} = {result}\n" # [f] this may be vuln., but we are learning

	# last-but-not-least
	print(fprint)


# Run app
if __name__ == "__main__":
	# l3ts make it automated
	isRunning = True
	ask = ""
	while isRunning:
		main()
		ask = input("Again?[Y/N] ")
		if ask.lower() != 'y':
			isRunning = False
