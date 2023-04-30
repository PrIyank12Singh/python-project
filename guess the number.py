import random
 l,u=map(int,input().split())
number=random.randint(l,u)
score=10
q=int(input("Enter your number:"))
while(number!=q or score<1):
    score=score-1
    if(q>number):
        print("close but less")
    elif(q<number):
        print("close but far")
    q=int(input("Cheerup,try one more time:"))
print("Good your score is:",score)
print("Your attempts were:",10-score)
