class sortWords():

    def sortInput(self, inputStr):
        words = [word.lower() for word in inputStr.split()]

        # sort the list
        words.sort()

        # display the sorted words

        # print("The sorted words are:")
        # for word in words:
        #     print(word)
        return words


# def main():
#     inputStr = input('Enter a string')
#     print(inputStr)
#     # inputStr = "Good Morning"
#     print(sortWords().sortInput(inputStr))


# main()
