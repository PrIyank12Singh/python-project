*******rock paper scissors*******
import random
name=input("Enter your name:")
print(f'''{name} Press start and let's start a game''')
co=0
a=1
while(a):
    c=input("Enter your choice:")
    l=['rock','paper','scissors']
    q=random.choice(l)
    if(q==c):
        print("You Wins")
        co+=1
    else:
        print("Try Again")
    print("Press again for another chance")
a=int(input())