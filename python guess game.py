import random
score=0
while True:
    a=random.randint(1,3)
    b=int(input("Enter a number "))
    if b>3:
        print("GAME OVER")
        break
    if b==a:
        print("Correct guess " + "Computer selected : ",a)
        score=score+10
        print("Your score : ",score)
    else:
        print("Number not same")
        print("Comp selected : ",a)
