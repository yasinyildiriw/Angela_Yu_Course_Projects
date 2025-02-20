import random

hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========
'''
hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========
'''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
'''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
'''
hangman4 = r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========
'''
hangman5 = r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========
'''
hangman6 = r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========
'''
hangman = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6]

words = ["aardvark", "baboon", "camel", "tiger", "snake", "mouse", "elephant"]
word = random.choice(words)
length_of_word = len(word)
empty_word = ['_']*length_of_word
live = 6
i=0
j=0
print(r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

while live > 0 :
    print(f"Word to guess: {empty_word}")
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in word :
        for i in range(len(word)):
            if word[i] == guess_letter:
                empty_word[i]=guess_letter
        print(f"{hangman[j]}")
        print(f"*************************************{live}/6 LIVES LEFT*************************************")

    else:
        live-=1
        j+=1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        print(f"{hangman[j]}")
        print(f"*************************************{live}/6 LIVES LEFT*************************************")
    if '_' not in empty_word:
        print("Congratulations! You won the game")
        break
    else:
        print(f"Game over the word should be {word}")

