import random

def playing(attempts):
    while(attempts > 0):
        resp = int(input("Pick a number: "))

        if(resp > number):
            attempts-=1
            print(f"Too high - attempts left {attempts}")
        elif (resp < number):
            attempts-=1
            print(f"Too low - attempts left {attempts}")
        elif (resp == number):
            print(f"You guessed it the number was {number}")
            break
        
        if (attempts == 0 and resp != number):
            print("You dont have any more chances to guess")

print("Welcome to the guessing game!")
print("Im thinking in a number between 1 and 100")
resp = input("Choose a dificulty level. ""easy"" or ""hard"": ").lower()

number = random.randint(1,100)
attempts = 0

if (resp == "easy"):
    attempts = 10
    playing(attempts)
elif (resp == "hard"):
    attempts = 5
    playing(attempts)
else:
    print ("wrong choice exiting")
