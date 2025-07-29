import random
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
print("Welcome to the password Generator !")
n_letters = int(input("How many letters you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
password = ""
for i in range(1, n_letters+1):
    char = random.choice(letters)
    password = password + char
for i in range(1, n_symbols+1):
    char= random.choice(symbols)
    password = password + char
for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    password = password + char
print(password)

