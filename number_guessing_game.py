import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("GUESS THE NUMBER BETWEEN 1 TO 100 : "))
        if guess > number: 
            print("Too High!")
        elif guess < number:
            print("Too Low!")
        else:
            print("Congratulations! You guess the number.")
            print(number)
            break
    except ValueError:
        print("Enter proper number")
