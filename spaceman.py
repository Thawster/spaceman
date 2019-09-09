from random import shuffle, choice
import os

# global variables 
alphabet = "abcdefghijklmnopqrstuvwxyz" 
wordlist = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = choice(words_list)
    return secret_word

def create_word(secret_word, index_guessed):

    with open('words.txt','r') as f:
        for line in f:
            for word in line.split():
                if len(word) == len(secret_word):
                    add_to_list = True
                    for index in index_guessed:
                        if word[int(index)] != secret_word[int(index)]:
                            add_to_list = False
                    for index in range(len(word)):
                        if index !=int(index_guessed[0]) and word[index] == secret_word[int(index_guessed[0])]:
                            add_to_list = False
                    if add_to_list:
                        wordlist.append(word)
    f.close()
 
def create_index_list(secret_word, letter_guessed):
    index_list= []
    for index in range(len(secret_word)):
        if secret_word[index] == letter_guessed:
            index_list.append(index)
    return index_list

def check_new_word(secret_word, letters_guessed, new_word):
    if len(secret_word) != len(new_word):
        return False
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
            if new_word[index] != secret_word[index]:
                return False
    for letter in new_word:
        if letter in letters_guessed:
            if letter in secret_word:
                pass
            else:
                return False
    return True

def randomize_word(secret_word, letters_guessed):
    shuffle(wordlist)
    for word in wordlist:
        if word == secret_word:
            pass
        elif check_new_word(secret_word, letters_guessed, word):
            return word
    else:
        return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    return True #Game Over


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else: 
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False


def not_guessed_string(guessed_letters):
    not_guessed_string=""
    for letters in alphabet:
        if letters in guessed_letters:
            pass
        else:
            not_guessed_string += letters
    return not_guessed_string


def spaceman(secret_word):
    guesses = len(secret_word)
    letters_guessed = ""
    print("Spaceman!")
    print("----------------------------------------")
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    print("You have " + str(guesses) + " incorrect guesses, please enter one letter per round")
    print("----------------------------------------")

    while guesses > 0 :
        input_valid = False
        while input_valid == False:
            guess = input("Enter a letter: ").lower()
            if guess in letters_guessed:
                print("You have already guessed " + guess + ".")
            elif len(guess) == 1 and guess.isalpha():
                input_valid = True
            elif len(guess) != 1:
                print("Please only enter one letter at a time")
            elif guess.isalpha() == False:
                print("Please only enter a letter")

        letters_guessed += guess
        os.system('clear')

        if is_guess_in_word(guess, secret_word):
            print("Your Guess appears in the word!")
            if len(wordlist) == 0:
                create_word(secret_word, create_index_list(secret_word, guess))
            secret_word = randomize_word(secret_word, letters_guessed)
        else:
            print("Your guess was not in the word. Try again")
            guesses -= 1

        if guesses > 0:
            print("You have " + str(guesses) + " incorrect guesses left")
            print("Guessed word so far: " + get_guessed_word(secret_word, letters_guessed))
            print("These letters haven't been guessed yet: " + not_guessed_string(letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                os.system('clear')
                print("You won!")
                break
            else:
                print("----------------------------------------")
        else:
            print("Sorry you didn't win, try again!")
            print("The word was: " + secret_word)
            break

def main():
    playing = True
    while playing == True:
        playing = False
        os.system('clear')
        spaceman(load_word())
        if input("Would you like to play again?(Y/N): ") in "Yy":
            playing = True
        else:
            print("Bye")

if __name__ == '__main__':
    main()
