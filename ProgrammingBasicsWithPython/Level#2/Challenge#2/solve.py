# Created by Mahros


# Loops Challenge
# Challenge#2

# data
fruits = [
    "apples",
    "bananas",
    "grapes",
    "mangos",
    "nectarines",
    "pears",
]


print("========== Task1 ==========")
# for loop to print all items
for value in fruits:
	print(value)


# some decoration
print("\n========== Task2 ==========")

# using while loop
index = 0
while index <= 4: # we can remove = if we want not to print the nect.
	print(fruits[index])
	index+=1

# output
#┌──(kali㉿DESKTOP-K00BQCF)-[~/…/AL-Mdrasa/Programming Basics with Python/Level#2/Challenge#2/]
#└─$ python3 solve.py
#========== Task1 ==========
#apples
#bananas
#grapes
#mangos
#nectarines
#pears

#========== Task2 ==========
#apples
#bananas
#grapes
#mangos
#nectarines
