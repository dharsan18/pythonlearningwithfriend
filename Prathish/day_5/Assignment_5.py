import random
from string import punctuation,ascii_letters
print("Welcome to random password generator!")
num=int(input("please enter length of the password?\n"))
char=int(input("please enter number of special characters?\n"))
nume=int(input("please enter number of numeric characters?\n"))
tot=num-char-nume
randomLetter =list(ascii_letters)
randomspecial=list(punctuation)
randomNumber=['1','2','3','4','5','6','7','8','9','0']
password=''
for x in range(1,num+1):
    if (char >=x):
        password+= random.choice(randomspecial)
    if(nume >=x):
        password+= random.choice(randomNumber) 
    if(tot >= x):
        password+=random.choice(randomLetter)
print( "Password:" +password)