import random
import RPi.GPIO as gpio
import time 

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.output(3,False)
gpio.output(7,False)
gpio.output(11,False)

def redlight():
    for i in range(12):
        time.sleep(0.1)
        gpio.output(3,True)
        time.sleep(0.1)
        gpio.output(3,False)
    # gpio.cleanup()

def greenlight():
    for i in range(12):
        time.sleep(0.1)
        gpio.output(7,True)
        time.sleep(0.1)
        gpio.output(7,False)
    # gpio.cleanup()

def buzzer():
    gpio.output(11,True)
    time.sleep(2)
    gpio.output(11,False)

lives=9
words =['write','big','help','axe','pumpkin']
secret_word=random.choice(words)
clue = []
index =0
heart =u'\u2764'
guessed_word_correctly=False
while index < len(secret_word):
    clue.append('?')
    index= index+1

def update_clue(guessed_letter,secret_word,clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter

        index = index + 1

while lives > 0:
    print(clue)
    if clue == list(secret_word):
        guessed_word_correctly = True
        break
    print("your lives: "+heart * lives)
    guess = input("Enter a letter or whole word: ")

    if guess in secret_word:
        print("letter found..")
        update_clue(guess,secret_word,clue)
        greenlight()
    else:
        print("incorrect guess. you lose a life")
        lives = lives -1
        redlight()

if guessed_word_correctly:
    print("you win.The secret word is [%s]"%secret_word)
    buzzer()
else:
    print("you lose.The secret word is [%s]"%secret_word)
    buzzer()

