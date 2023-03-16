def main():
    word_dictionary = {
        "hi": "a way to greet",
        "martial": "a worrier or ready for war",
        "left": "direction"
    }
    while (True):
        word = input("enter the word: ")
        if word == "":
            break
        else:
            print(word, ":", word_dictionary[word])


main()
