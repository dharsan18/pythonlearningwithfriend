print("Welcome to the tip calculator!")
rate=int(input("What was the total bill ? $"))
tip= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
if (tip==10):
    t=int(rate*(tip/100))
elif(tip==12):
    t=int(rate*(tip/100))
elif(tip==15):
    t=int(rate*(tip/100))
count=int(input("How many people to split the bill? "))
pay= int((rate+t)/count)
print(f"EaAssch person should pay: ${pay} ")
    
    