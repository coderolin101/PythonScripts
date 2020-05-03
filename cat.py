# from sys import argv

# script, name, age = argv

# The above statements or values or modules are not needed because 
# this is a demonstration of the class and main execution in Python3.

class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def info(self):
		print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
	def make_sound(self):
		print("Meow!")

def main():
	cat1 = Cat('Andy',2)  # The above class is called and instantiated
	cat2 = Cat('Phoebe',3)
	cat1.info()  # The calss variable is called and then its function.
	cat1.make_sound()
	cat2.info()
	cat2.make_sound()

main()  # Remember that main is always called last.
