
#Hangman
import random
maxTry = 10
words = ['python', 'house', 'sun', 'immortal']
chosenWord = random.choice(words)
displayWord = ("_" * len(chosenWord))
print(displayWord)
while ('_' in  displayWord):
    if maxTry == 0:
        print("ცდების რაოდენობა ამოიწურა")
        exit()
    userInput = input('შეიყვანეთ ასობგერა \n \n')
    if  userInput in chosenWord:
        indexes = ([index for index, char in enumerate(chosenWord) if char == userInput])
        displayWord = list(displayWord)
        for item in indexes:
            displayWord[item] = userInput
        displayWord = ''.join(displayWord)
        print('არის ასეთი ასობგერა ',displayWord)
    else:
        print('არ არის ასეთი ასობგერა ',displayWord)
    maxTry -= 1

print("გილოცავთ გამოიცანით ")
        