# Created by Mahros


# Info
# Challenge#2



# input
first_number 	= input("First number: ")
second_number = input("Second number: ")
operator			= input("Enter sign: ")

# make them numbers not strings
first_number = float(first_number)
second_number= float(second_number)


# process
out = 0.0 # this will be the box of the calc. result

if operator == '+': 		# addition
	out = first_number + second_number
elif operator == '-': 	# subtraction
	out = first_number - second_number
elif operator == '*': 	# multiplication
	out = first_number * second_number
elif operator == '/': 	# division
	out = first_number / second_number
elif operator == '//': 	# strict devision
	out = first_number // second_number
elif operator == '**': 	# power
	out = first_number ** second_number
elif operator == '%': 	# mod
	out = first_number % second_number
else:
	out = 0.0
	print(f"Invalid operator({operator})")

# output
print("Formula>", first_number, operator, second_number, "=", out)

# console
#┌──(kali㉿DESKTOP-K00BQCF)-[~/…/AL-Mdrasa/Programming Basics with Python/Challenges/Challenge#2]
#└─$ python3 solve.py
#First number: 1
#Second number: 5
#Enter sign: +
#Formula> 1.0 + 5.0 = 6.0

#┌──(kali㉿DESKTOP-K00BQCF)-[~/…/AL-Mdrasa/Programming Basics with Python/Challenges/Challenge#2]
#└─$ python3 solve.py
#First number: 1
#Second number: 5
#Enter sign: /
#Formula> 1.0 / 5.0 = 0.2

#┌──(kali㉿DESKTOP-K00BQCF)-[~/…/AL-Mdrasa/Programming Basics with Python/Challenges/Challenge#2]
#└─$ python3 solve.py
#First number: 1
#Second number: 5
#Enter sign: //
#Formula> 1.0 // 5.0 = 0.0
