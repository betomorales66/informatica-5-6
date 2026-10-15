#create a TXT file with all of the words
#define the main function
#print a welcome to the gem
#make and input to see if you want to neter the game
#if you choose yes it enters the game
#if you chose no it leads you to a screen that says thank you
#call start_game function
#make the program choose a random word from the TXT file
#use len to acomodate the fuction
#make a attempt counter variable
#make the program choose a random word from the TXT file
#use with to open the TXT file
#define words file
#write if it matcehs all of the words congratulaions
#put thank you for playing!
import random


def main():
    start_game("words.txt")

def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()

    word = random.choice(word_bank)
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")
        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break
    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)


if __name__ == "__main__":
    main()
