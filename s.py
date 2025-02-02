import random

def game():
    num = random.randrange(1,20)
    user = input("Hello! What is your name?\n")
    print(f"Well, {user}, I am thinking of a number between 1 and 20")
    i = 1
    x = int(input("Take a quess.\n"))
    while x != num:
            if x < num:
                print("Your guess is too low.")
            elif x > num:
                print("Your guess is too high.")
            x = int(input("Take a guess.\n"))
            i += 1
    print(f"Good job, {user}! You guessed my number in {i} guesses!")
            
        

game()
        

    
    