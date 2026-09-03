import random
def main():
    name = input("Helo, what is your name? ")
    print(F"well, {name}, I am thinking of a number between 1 and a 100.")

    # start game with random number
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("take a guess: "))
        if guess > number:
            print("your guess is too high.")
        elif guess < number:
            print("your guess is too low.")

    print(F"good little boy, {name}! you guessed it!")




if __name__=="__main__":
    main()
