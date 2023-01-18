from string import punctuation,ascii_letters
from random import choice
symbols_list = list(punctuation)
numbers_list = ['0','1','2','3','4','5','6','7','8','9']
alphabets_list = list(ascii_letters)

def generate_password(length_of_password: int,symbols: int,numbers: int) :
    if length_of_password < symbols + numbers :
        raise Exception("Entered Symbols and Number value is more than the length of password")
    password = ''
    for i in range (1,length_of_password+1):
        if symbols >= i : 
            password += choice(symbols_list)
        if numbers >= i : 
            password += choice(numbers_list)
        if length_of_password - symbols - numbers >=i :
            password += choice(alphabets_list)
    print("\nGenerated Password: "+ password)

if __name__ == "__main__":
    print("Welcome to the password generator!\n")
    length_of_password = int(input("Please enter the length of the password: "))
    special_characters = int(input("Please enter the number of special characters: "))
    numbers = int(input("Please enter the number of numeric characters: "))
    generate_password(length_of_password,special_characters,numbers)
    
    