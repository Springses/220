'''
Elijah Springs

hw9.py

This program is supposed to create a hangman game. Though I couldn't figure out the GUI portion, this is what I
attempted.

This is my work.
'''

# imports
from random import randint

def get_words(file_name):

    # opens file
    word_file = open(file_name, "r")

    # creates list
    w = word_file.read()
    list_of_words = w.splitlines()

    # returns list
    return list_of_words

def get_random_word(words):

    # store amount of words
    amount_of_words = len(words)
    # generate random number
    num = randint(0, amount_of_words - 1)
    random_word = words[num]
    # return random number
    return random_word


def letter_in_secret_word(letter, secret_word):

    # if letter is more than one character, it returns false.
    if len(letter) > 1:
        return False
    # if letter, doesn't appear, it returns false.
    elif secret_word.count(letter) < 1:
        return False
    else:
        return True


def already_guessed(letter, guesses):

    # if guesses contain that letter, it returns true.
    if guesses.count(letter) >= 1:
        return True
    return False


def make_hidden_secret(secret_word, guesses):

    # accumulators
    secret_word_hidden = ""
    finder = 0

    # creates blank underscores.
    for i in secret_word:
        secret_word_hidden = secret_word_hidden + "_ "

    # goes through each guessed letter
    for letter in guesses:
        # if letter appears
        if letter_in_secret_word(letter, secret_word):
            # if letter only occurs once
            if secret_word.count(letter) < 2:
                finder = secret_word.find(letter)

                secret_word_hidden = secret_word_hidden.replace(" ", "")
                secret_word_hidden = list(secret_word_hidden)

                secret_word_hidden[finder] = letter

                new_hidden_word = ""

                for j in range(len(secret_word_hidden)):
                    indexer = secret_word_hidden[j]
                    new_hidden_word = new_hidden_word + indexer
                    new_hidden_word = new_hidden_word + " "

                secret_word_hidden = new_hidden_word

            # if letter appears twice
            else:
                for k in range(secret_word.count(letter)):
                    finder = secret_word.find(letter, finder)

                    secret_word_hidden = secret_word_hidden.replace(" ", "")
                    secret_word_hidden = list(secret_word_hidden)

                    secret_word_hidden[finder] = letter

                    new_hidden_word = ""

                    for l in range(len(secret_word_hidden)):
                        indexer = secret_word_hidden[l]
                        new_hidden_word = new_hidden_word + indexer
                        new_hidden_word = new_hidden_word + " "

                    secret_word_hidden = new_hidden_word

                    finder = finder + 1

    return secret_word_hidden

def won(guessed):
    # if there are no underscores, the user has one.
    if guessed.count("_") == 0:
        return True
    return False


def play_graphics(secret_word):
    # couldn't figure this out :(
    pass


def play_command_line(secret_word):
    # start up settings.
    guessed = []
    remain_guess = 6
    hidden_word = make_hidden_secret(secret_word, guessed)

    while remain_guess > 0 and won(hidden_word) == False:
        # prints lines like which letters are guessed, how many guesses left, and hidden word.
        print("Already guessed: ", guessed)
        print("Remaining guesses: ", remain_guess)
        print(hidden_word)
        entry_letter = input("Guess a letter: ")

        # in case they have caps lock.
        entry_letter = entry_letter.strip()
        entry_letter = entry_letter.lower()

        # if the letter is already guessed, it loops until a new letter is inputted.
        if already_guessed(entry_letter, guessed):
            while already_guessed(entry_letter, guessed):
                entry_letter = input("That one is already guessed, choose another: ")
                entry_letter = entry_letter.strip()
                entry_letter = entry_letter.lower()

        # adds entry letter to the guessed letters.
        guessed.append(entry_letter)
        #   if letter is in the hidden word, it adds it to the hidden word.
        if letter_in_secret_word(entry_letter, secret_word):
            hidden_word = make_hidden_secret(secret_word, guessed)
        else:
            remain_guess = remain_guess - 1

    # if remaining guesses reaches 0, the user loses, otherwise they have won.
    if remain_guess == 0:
        print("sorry, you weren't able to guess the word: ")
        print(secret_word)
    else:
        print("You won!")
        print(secret_word)




if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
