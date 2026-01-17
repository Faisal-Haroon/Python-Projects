import random

while True:  
    number = random.randint(1, 100) 
    attempts = 0
    max_attempts = 5
    
    while True:  
        if attempts >= max_attempts:
            print(f"Game over! Number was {number}")
            break
        
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You guessed it in {attempts} attempts.")
            break
    

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
