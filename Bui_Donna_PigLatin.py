# Sequences Part 2: Pig Latin - Donna Bui - 3/15/2023 - Professor Henry Estrada's COMSC 078
# This program accepts a sentence as input and converts each word in the sentence to “Pig Latin.”
# ----------------------------------------------------------------
# Expected Outputs:
# Python is a programming language → ythonpay isway away ogrammingpray anguagelay
# <#Python$>, Is. A! % "prOgramming' Language?; → ythonpay isway away ogrammingpray anguagelay
# Your strong ox plows the field → yourway ongstray oxway owsplay ethay ieldfay
# Hlllo trhr crshrw → ohlllay trhray crshrway

import string

vowels = ['a','e','i','o','u','y'] # List of all vowels. Number characters are considered consonants.

def pigLatinify(userInput):
    userInput = userInput.translate(str.maketrans('', '', string.punctuation)) # Remove all punctuation from the string
    words = userInput.split() # Make a list containing all the words in the string
    convertedWords = [] # List to store all the words converted to Pig Latin
    for word in words: # Iterate through every word in the list containing the user's input
        convertedWord = word.lower() # Convert the word to all lowercase
        if convertedWord[0] in vowels: # If the first letter of the word is a vowel,
            convertedWord += "way" # Add "way" to the end of the word
        else:
            lettersMoved = 0
            while not convertedWord[0] in vowels and lettersMoved < len(convertedWord): # If there are consonants,run loop until the first letter becomes a vowel. Works with any number of consonants.
                convertedWord = convertedWord[1:] + convertedWord[0] # string[1:] is like Java substring; it returns all characters starting from the given index. 
                lettersMoved += 1 # If we end up with a word that consists of only consonants, the loop won't just run infinitely. It will stop once the end of the word is reached and return the word as it is.
            convertedWord += "ay" # After all consonants are moved to the end, add "ay" to the end of the word
        convertedWords.append(convertedWord) # Add the newly converted word to the list of converted words
    return convertedWords

while True: # Similar to a do-while loop in Java, but since Python doesn't have a do-while loop, this uses break to stop the loop when the stop condition is met.
    userInput = input("Enter a word or phrase to convert to Pig Latin (press ENTER to stop): ")
    if userInput == "": # Input is automatically blank when the user presses ENTER without typing anything
        print("Program stopped. To resume using, simply restart the program.")
        break
    else:
        print(*pigLatinify(userInput))