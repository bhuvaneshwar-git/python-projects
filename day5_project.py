#easy method

import random
print("Password Generator Project")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# letters_store = ""

# for value in range(0,nr_letters):
#     len_letters = len(letters)
#     value = random.randint(0,len_letters)
#     letters_value = letters[value-1]
#     letters_store+=letters_value
#     # print(letters_value,end="")

# for value_1 in range(0,nr_symbols):
#     len_symbols = len(symbols)
#     value_1 = random.randint(0,len_symbols)
#     symbols_value = symbols[value_1-1]
#     letters_store+=symbols_value
#     # print(symbols_value,end="")

# for value_2 in range(0,nr_numbers):
#     len_numbers = len(numbers)
#     value_2 = random.randint(0,len_numbers)
#     numbers_value = numbers[value_2-1]
#     letters_store+=numbers_value
#     # print(numbers_value,end="")
# print(letters_store)


letters_store = []


for value in range(0,nr_letters):
    len_letters = len(letters)
    value = random.randint(0,len_letters)
    letters_value = letters[value-1]
    letters_store+=letters_value
    

for value_1 in range(0,nr_symbols):
    len_symbols = len(symbols)
    value_1 = random.randint(0,len_symbols)
    symbols_value = symbols[value_1-1]
    letters_store+=symbols_value
    

for value_2 in range(0,nr_numbers):
    len_numbers = len(numbers)
    value_2 = random.randint(0,len_numbers)
    numbers_value = numbers[value_2-1]
    letters_store+=numbers_value
    
# print(letters_store)
random.shuffle(letters_store)
# print(letters_store)
password =  ""
for value_3 in letters_store:
    password = password+value_3
print(f"your password is : {password}")



