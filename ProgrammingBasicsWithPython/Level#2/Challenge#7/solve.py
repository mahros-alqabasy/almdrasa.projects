# Created by Mahros



# Dependencies
import re


def trim(plain:str):
	regex = r"\s{2,}"
	return re.sub(regex, "\n", plain, )


class Cat:
	def __init__(self, name, color, age, speed=[0, 0]):
		self.color 					= color
		self.name  					= name
		self.age						= age
		self.speed					= speed

	def unit(self, speed:int):
		return f"{speed}hop/sec"

	def rspeed(self):
		return self.unit(self.speed[0])

	def wspeed(self):
		return self.unit(self.speed[1])

	def run(self):
		print(f"I can run {self.rspeed()}")

	def walk(self):
		print(f"I can walk {self.wspeed()}")

	def toString(self):
		result = f"""
Hi,
I am a {self.color} Cat.
My name is {self.name}.
I have {self.age} years old.
I can run {self.rspeed()}.
I can walk {self.wspeed()}.
Bye, Bye.
		"""
		return result

	def display(self):
		print(self.toString())


# test it
cats = [
	Cat("Hanafy", "Yellow", 6, [20, 3]),
	Cat("Semsema", "Whaite", 3, [50, 10]),
	Cat("Antar", "Black", 9, [100, 1])
]

for cat in cats:
	print("=" * 5, cat.name, "="*5)
	cat.display()
