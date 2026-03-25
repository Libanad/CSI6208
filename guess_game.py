# Liban Adhikari
# 10714736
# I have pushed this code in github as well GITHUB LINK: https://github.com/Libanad/CSI6208.git
# Guess Game Assignment

import random


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


    print("Welcome to Guess Game!")

    while True:

        wordList = random.sample(candidateWords, 8)
        password = random.choice(wordList)

        guessesRemaining = 4
        won = False
        guessedWords = {}

        while guessesRemaining > 0 and not won:

            print("\nWord List:")

            for i in range(len(wordList)):
                word = wordList[i]
                if word in guessedWords:
                    print(i + 1, ".", word, "-", guessedWords[word], "/6")
                else:
                    print(i + 1, ".", word)

            print("Guesses Remaining:", guessesRemaining)

            try:
                choice = int(input("Enter word number (1-8): ")) - 1

                if choice < 0 or choice >= 8:
                    print("Invalid input")
                    continue

            except:
                print("Invalid input")
                continue

            guess = wordList[choice]

            if guess in guessedWords:
                print("You already guessed this word")
                continue

            guessesRemaining -= 1

            if guess == password:
                print("Password Correct!")
                won = True
            else:
                match = compareWords(password, guess)
                guessedWords[guess] = match
                print("Password Incorrect")
                print(match, "/6 letters correct")


        if won:
            print("You Win!")
        else:
            print("You Lose!")
            print("Password was:", password)


        playAgain = input("Play again? (yes/no): ").lower()

        if playAgain != "yes":
            print("Thanks for playing!")
            break


main()