import random
print("Welcome to Stone, Paper, Scissor Game\n 1 --> Stone\n 2 --> Paper\n 3 --> Scissor")
user= int(input("Enter the Number: "))
mac = random.randint(1,3)
if(mac == 1):
    com ="Stone"
elif(mac == 2):
    com="Paper"
elif(mac == 3):
    com = "Scissor"
if (user ==1 and mac ==1):
    print("Match is draw!")
elif((user == 1 and mac ==2)or(user==2 and mac ==3 )or(user==3 and mac ==1 )):
    print(f"User loss! com: {com}")
elif((user == 2 and mac == 1)or(user == 3 and mac == 2)or(user == 1 and mac == 3)):
    print(f"User won!  com: {com}")
else:
    print('invalid input')
    
