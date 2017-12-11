# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import os

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

#%%
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    checker = []
    for letter in secretWord:
        if letter in lettersGuessed:
            checker.append(True)
        else:
            checker.append(False)
            break
    return(all(checker))


isWordGuessed('llama', ['m', 'a'])
isWordGuessed('llama', ['m', 'a', 'l'])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '_ ')
    return(secretWord)

getGuessedWord('llama', ['m'])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in availableLetters:
        if letter in lettersGuessed:
            availableLetters = availableLetters.replace(letter, '_')
    return(availableLetters)

getAvailableLetters(['a', 'b', 'c'])




def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    # Initialize game variables
    lettersGuessed = []
    numGuesses = 8


    # Starting message
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) +
          ' letters long.')

    # Start the game. The game runs until you win or run out of guesses
    while True:
        # Messages
        print('')
        print('--------------')
        print('You have ' + str(numGuesses) + ' guesses left')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))

        guess = input('Please guess a letter: ')
        guess = guess.lower()

        # If letter was already guessed, give feedback and repeat
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                  str(getGuessedWord(secretWord, lettersGuessed).upper()))

        # If guessed letter correctly, check if they've won yet.
        # If not, continue the game.
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: ' +
                  str(getGuessedWord(secretWord, lettersGuessed).upper()))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                break

        # If guessed wrong, decrement guesses and continue the game
        else:
            lettersGuessed.append(guess)
            numGuesses -= 1
            print("Oops! That letter is not in my word: " +
                  str(getGuessedWord(secretWord, lettersGuessed).upper()))
            if numGuesses == 0:
                print('Sorry, you ran out of guesses. The word was ' +
                      str(secretWord) + '.')
                break


#%%


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
