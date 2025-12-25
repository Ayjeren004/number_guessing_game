import random
lowest=1
highest=10

answer=random.randint(lowest,highest)
guesses=0
is_running=True #while user is playing the game
print("Welcome to the Number Guessing Game!")

print(f'Select a number between {lowest} and {highest}')

while is_running:
    guess=input("Please enter your guess:")
 
    if guess.isdigit():
        #if the value is number
        guesses+=1
        guess=int(guess)
        if guess in range(lowest,highest+1):
            if guess==answer:
                print(f"Nice!You won! The number was {answer}! It took to you {guesses} to get the correct number!")
                is_running=False
            elif guess>answer:
                print("Too high")
             
            elif guess<answer:
                print("Too low")
               
        else:
            print(f"Please choose a number a number {lowest} and {highest}")
    else:
        print("Please input a number!")
        


