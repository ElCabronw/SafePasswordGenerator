#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = nr_letters + nr_symbols + nr_numbers


finalPassword = ""
 
finalPassword2 = []

letcount = 0
symbCount = 0
numbCount = 0
for letter in letters:
    finalPassword2.append(random.choice(letters))
    letcount += 1
    if letcount == nr_letters:
        break

for symbol in symbols:
    finalPassword2.append(random.choice(symbols))
    symbCount += 1
    if symbCount == nr_symbols:
        break

for number in numbers:
    finalPassword2.append(random.choice(numbers))
    numbCount += 1
    if numbCount == nr_numbers:
        break

random.shuffle(finalPassword2)
print(''.join(finalPassword2))
