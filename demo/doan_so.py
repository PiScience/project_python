import random
yes="YES"
question=input("Do you want to play a game?Yes/No:")
while question.upper()==yes:
    d=int(input("Enter the number range:"))
    a=int(input("enter amount of guesses you are allowed to take:"))
    b=random.randint(1,d)
    for i in range(a):
        guess=int(input("Please enter the amount of number from 1-{}:".format(d)))
        if b>guess:
            print("Your number is smaller than number generated")
        elif guess==b:
            print("You guessed it the number was "+str(b))
            break
        else:
            print("Your number is larger than number generated")
    question=input("Do you want to retry the game?Yes/No:")
print("Ok see you again!")
