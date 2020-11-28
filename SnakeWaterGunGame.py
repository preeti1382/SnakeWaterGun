import random

lst = ["w" , "g" , "s"]
t = 10
bpoint = 0
upoint = 0
print("\n WELCOME TO THE GAME\n")
while t!=0 :
    user = input("enter your choice of snake water and gun as 's' , 'w' or 'g':\n")
    b = random.choice(lst)
    if user == "s" and b == "w" :
        upoint = upoint + 1 
        print("You got 1 point\n computer's choice was:" , b)
    elif user == "w" and b == "s" :
        bpoint = bpoint + 1
        print("Computer got 1 point\n computer's choice was:" , b)
    elif user == "g" and b == "s" : 
        upoint = upoint + 1
        print("You got 1 point\n computer's choice was:" , b)
    elif user == "s" and b == "g" :
        bpoint = bpoint + 1
        print("Computer got 1 point\n computer's choice was:" , b)
    elif user == "w" and b == "g" :
        upoint = upoint + 1
        print("You got 1 point\n computer's choice was:" , b)
    elif user == "g" and b == "w" :
        bpoint = bpoint + 1
        print("Computer got 1 point\n computer's choice was:" , b)
    elif user == "s" and b == "s" :
        print("both chose same option!\n computer's choice was:" , b)
    elif user == "w" and b == "w" :
        print("both chose same option\n computer's choice  was:" , b)
    elif  user == "g" and b == "g" :
        print("both chose the same option!\n computer's choice was:" , b)
    else :
        print("invalid choice...\n")

    t = t - 1
    
    
print(f"Computer Score: {bpoint} \n  Your Score: {upoint}")
if upoint > bpoint :
        print("You are the winner!!\n")
elif bpoint > upoint :
        print("Computer is the winner!!\n")
else :
        print("Game tie!!\n")