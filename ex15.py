from sys import argv #taking a argv module/feature/library from package sys

script, filename = argv

txt = open(filename) #WILL create  a file object.

print(f"Here's your file {filename}:") #printing format variables.
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
