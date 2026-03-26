# Liban Adhikari
# 10714736
# Guess Game Assignment

import random
from guess_utils import compareWords, displayWordList, validateInput, playAgain


def main():

    candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER',
    'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER',
    'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED',
    'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER',
    'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER',
    'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER',
    'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER',
    'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER',
    'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER',
    'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER',
    'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER',
    'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER',
    'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']


    print("Welcome to Guess Game!")

    while True:

        wordList = random.sample(candidateWords, 8)
        password = random.choice(wordList)

        guessesRemaining = 4
        won = False
        guessedWords = {}

        while guessesRemaining > 0 and not won:

            displayWordList(wordList, guessedWords)

            print("Guesses Remaining:", guessesRemaining)

            choice = validateInput()

            if choice is None:
                continue

            guess = wordList[choice]

            if guess in guessedWords:
                print("You already guessed this word")
                continue

            guessesRemaining -= 1

            if guess == password:
                print("The Password Is Correct!")
                won = True
            else:
                match = compareWords(password, guess)
                guessedWords[guess] = match
                print("The Password is Incorrect")
                print(match, "/6 letters correct")

        if won:
            print("Congratulationnnnn You Win!")
        else:
            print("Sorry You Lose!")
            print("Password was:", password)

        if not playAgain():
            print("Thanks for playing!")
            break


main()