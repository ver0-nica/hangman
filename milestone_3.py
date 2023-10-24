import random

word_list = ['apple', 'pear', 'banana', 'watermelon', 'chestnut']
#print(word_list )

word = random.choice(word_list)
#print(word)



def check_guess(guess):
 guess.lower()
 if guess in word:
  print('Good guess!', guess, 'is in the word.')
 else:
  print('Sorry,', guess, 'is not in the word, try again.')
  
def ask_for_an_input(): 
 while True:
   guess = input('Enter a single letter ')
   if guess.isalpha() == True and len(guess) == 1:
     break
   else:
     print('Invalid letter. Please, enter a single alphabetical character.')
 check_guess(guess)

ask_for_an_input()



    