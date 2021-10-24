import random

print("NUMBER GUESSING GAME")
print("Try to guess the number.")

tries = 0

number = random.randint(1, 9)

while(tries < 5):
    guess = int(input("Enter you guess it must be between 1 and 9. "))

    if(guess == number):
        print("You won this time.")

    elif(guess > number):
        print("Your guess was too high.")

    else:
        print("Your guess was too low.")

    tries = tries + 1

if(tries > 5):
    print("You lost, the number was", number, ".")