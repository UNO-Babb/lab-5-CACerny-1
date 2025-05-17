#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""

    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    rated_word = ""
    for i, letter in enumerate(myGuess):
        if inSpot(letter, word, i):
            rated_word += letter.upper()
        elif inWord(letter, word):
            rated_word += letter.lower()
        else:
            rated_word += '*'
    return rated_word

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    attempts = 6

    print("WORD GAME")
    
    while attempts > 0:
        guess = input(f"Guess the 5-letter word ({attempts} attempts left): ")
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        rated_guess = rateGuess(guess, todayWord)
        print("Rated Guess: ", rated_guess)
        if guess == todayWord:
            print("Congratulations! You've guessed the correct word!")
            break
        attempts -= 1

    if attempts == 0:
        print("Sorry, you are out of attempts. The word was ", todayWord, ".")


    #User should get 6 guesses to guess

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
