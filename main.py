import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")
number_of_letters= int( input("How many letters would you like in your password?\n") ) 
number_of_symbols = int( input("How many symbols would you like?\n") )
number_of_numbers = int( input("How many numbers would you like?\n") )

password = ""
password_list = random.choices(letters, k = number_of_letters) + random.choices(symbols, k = number_of_symbols) + random.choices(numbers, k = number_of_numbers)
random.shuffle(password_list)
for character in password_list:
    password += character
print(f"Your Password is : {password}")