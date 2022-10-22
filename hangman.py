from itertools import count
import random
from sys import displayhook
import time

print('\n Welcome to Hangman Game by Userking\n')
name = input('Enter your name:')
print('hi there '+name+'! best of luck')
time.sleep(2)
print('The game is about to start!\n Lets play Hangman!')
time.sleep(3)

def main():
    global count
    global word
    global already_guessed
    global display
    global length 
    global play_game
    words_to_guessed = ['january','february','march','april','may','june','july','august','september','october','november','december']
    word = random.choice(words_to_guessed)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''
def play_loop():
    global play_game
    play_game = input('do you want to play again? y = yes , n = no\n')
    while play_game not in ['y','Y','n','N']:
        play_game = input('do you want to play again? y = yes , n = no\n')
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print('Thanks for playing Hangman! we expect you again')
        exit()
    
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit  = 5
    guess = input('This is the hangaman word:'+ display + 'Enter your guess: \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()