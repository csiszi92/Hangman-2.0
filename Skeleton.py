import random
import sys

def beginning():
    print("Welcome!")
    while True:
        name = input("Enter your name: ")
        print("Hello", name + "!")
        if name == "":
            print("You have to type something!")
        else:
            break
beginning()

capitals = ['LONDON', 'AMSTERDAM', 'BUDAPEST', 'Valami Valami Valami']
capital = random.choice(capitals)
print(capital)
all_letters = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
used_letters = []


def get_hashed():
    hide = ""
    for letter in capital:
    # doesnt replaces spaces with dash
        if letter != " ":
            hide = hide + "_"
        else:
            hide = hide + " "
    print("Your secret word is " + hide)
get_hashed()

def input_letter():
    guess = input("Pick a letter:\n").upper()
    if not guess in all_letters: 
            print("Please enter a letter from the alphabet(a-z)!")
    elif guess in used_letters: 
            print("You have already used that letter, please pick another!")
    else:
        used_letters.append(guess)
        if guess in capital:
            print("You found a letter.")
            
    return used_letters
input_letter()

#def update():
  


#def uncover():

