import random

my_favourite_fruits = ['apple', 'pear', 'banana', 'watermelon', 'chestnut']
word_list = my_favourite_fruits
print(word_list )

choice = random.choice(word_list)
word = choice
print(word)

guess = input('Enter a single letter ')
if len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! that is not a valid input')
