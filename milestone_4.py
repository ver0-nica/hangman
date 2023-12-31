import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        
        self.list_of_guesses = [ ]
        
        self.word_guessed = ['_' for i in range(len(self.word))]

        self.num_of_letters = 0
    def check_guess(self, guess):
         guess.lower()
         if guess in self.word:
          print('Good guess!', guess, 'is in the word.')
          for letter in self.word:
             if letter == guess:
                i = self.word.index(letter)
                self.word_guessed[i] = letter
          self.num_of_letters -= 1
         else:
          self.num_lives -= 1
          print('Sorry,', guess, 'is not in the word, try again.')
          print('You have', self.num_lives, 'lives left')
        
    
    def ask_for_an_input(self):
       while True:
          guess = input('Enter a single letter ')
          if guess.isalpha() == False or len(guess) != 1: 
             print('Invalid letter. Please, enter a single alphabetical character.') 
          elif guess in self.list_of_guesses:
             print('You have already tried that letter!')
          else:
             self.check_guess(guess)
             self.list_of_guesses.append(guess)

my_word_list = ['apple', 'pear', 'banana', 'watermelon', 'chestnut']
my_hangman = Hangman(my_word_list)
my_hangman.ask_for_an_input()
