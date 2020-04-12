#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hangman by <your name> 2018

def replaceWithHyphens(phrase):
    newPhrase = ""
    for n in range(len(phrase)):
        if (phrase[n] == " "):
            newPhrase = newPhrase + " "
        else:
            newPhrase = newPhrase + "-"
    return(newPhrase)

def tryGuessedLetter(secretPhrase, letter, partialPhrase):
    newPhrase = ""
    for n in range(len(secretPhrase)):
        if (letter == secretPhrase[n]):
            newPhrase = newPhrase + letter
        else:
            newPhrase = newPhrase + partialPhrase[n]
    return(newPhrase)
   
secretPhrase = "penguin"
lettersUsed = ""
guessesLeft = 10
partialPhrase = replaceWithHyphens(secretPhrase)
print("Can you guess this phrase ?")
win = False

while(guessesLeft > 0):
    print("")
    print(partialPhrase)
    print("Letters used: " + lettersUsed)
    letter = input("You have " + str(guessesLeft) + " guesses left, enter a letter: ")
    guessesLeft = guessesLeft - 1
    lettersUsed = lettersUsed + letter
    partialPhrase = tryGuessedLetter(secretPhrase, letter, partialPhrase)
    
    if (partialPhrase == secretPhrase):
        print("")
        print("Congratulations - you guessed correctly!")
        win = True
        break
    
if (win != True):
    print("")
    print("You failed - the answer was: " + secretPhrase)
    


# In[ ]:




