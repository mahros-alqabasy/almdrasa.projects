# Created by Mahros


# Dependencies
import re


# plain text
string = """
almdrasa is your way to learn programming the right way. almdrasa badges motivate students to do more. almdrasa quizzes help students practice on what they have learned through the course. almdrasa courses are one of a kind because they were made by professionals. almdrasa look and feel is one of a kind. almdrasa wishes you a good learning. thanks.
"""

# make it as a reusable
def solution(text:str, repl:str, count:int):
	regex = r"almdrasa \w{3,}"
	return re.sub(regex, repl, text, count=count)



# output
print(solution(string, "Almdrasa", 3))
