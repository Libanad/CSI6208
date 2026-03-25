# Liban Adhikari
# 10714736
# Come on Let's Play a guessing game with me

import random


# Function to compare two words
def compareWords(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return count


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


    print("Welcome to the Guess Game!")

   
    while True:

        secretWord = random.choice(candidateWords)

        print("\nGuess the 6-letter word")

        while True:
            guess = input("Enter your guess: ").upper()

           
            if len(guess) != 6:
                print("Please enter a 6-letter word.")
                continue

            match = compareWords(secretWord, guess)

            if guess == secretWord:
                print("Correct! You guessed the word:", secretWord)
                print("Starting new game...")
                break
            else:
                print("Matching letters in correct position:", match)

        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain != "yes":
            print("Thanks for playing!")
            break
main()