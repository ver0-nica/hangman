# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
In order to play the game you just need to pass the function 'play_game'  to a list of words. This function create an istance of the class Hangman, expressely defined to play this game. The attributes and methods of this class are called within the function.  

The Hangman class is made of six attributes and two methods. In order to create an istance of the class you havve to pass a word_list and the number of lives of the player, which is set to five by default. Then the other attributes are a word chosen randomly in your list, a list of guesses and a list containing the guessed  letters. 
The first method is called chek_guess and it checks if the letter chosen is in your word,and if it's not it decreases the number of lives of  one. The second method, instead, ask for the user to enter a letter, and if it's a valid input, it runs the check guess method.
