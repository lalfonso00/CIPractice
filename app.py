
def main():
    inputStr = input('Enter a string')

    words = [word.lower() for word in inputStr.split()]

    # sort the list
    words.sort()

    # display the sorted words

    print("The sorted words are:")
    for word in words:
        print(word)


main()
