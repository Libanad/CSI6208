# Liban Adhikari
# 10714736
#I HAVE UPLOADED THE CODE ON GITHUB checkit out https://github.com/Libanad/CSI6208.git
# Guess Game Assignment
#Come let's play the game together
def compareWords(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return count


def displayWordList(wordList, guessedWords):
    print("\nWord List:")
    for i in range(len(wordList)):
        word = wordList[i]
        if word in guessedWords:
            print(i + 1, ".", word, "-", guessedWords[word], "/6")
        else:
            print(i + 1, ".", word)


def validateInput():
    try:
        choice = int(input("Enter word number (1-8): ")) - 1

        if choice < 0 or choice >= 8:
            print("The number must be between 1 and 8. Invalid input")
            return None

        return choice

    except:
        print("Invalid input")
        return None


def playAgain():
    answer = input("Do You want to play again? (yes/no): ").lower()
    return answer == "yes"