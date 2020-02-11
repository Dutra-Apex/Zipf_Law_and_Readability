# Character & Word count - Gabriel Ferreira Dutra
# Function 'count()' prints the frequency of every word as a dictionary and the frequency of every character as an array


def count():
    file = open("Turing.txt", "rt")
    text = (file.read()).lower()  # Reads the file once, changes it to lowercase and stores it on a variable "text"
    file.close()

    text = text.replace(",", " ")  # Removes all commas on text
    text = text.replace(".", " ")  # Removes all periods on text

    words = text.split()  # Defines a list of words by using the split method on the file
    word_count = 0
    dict_w = {}

    # Nested loop that runs through the list of words
    for i in range(len(words)):
        for j in words:
            if j == words[i]:
                word_count += 1  # Add one for every time a word from the list appears on the text

        dict_w[words[i]] = word_count  # Creates a dictionary associating each word to its frequency
        word_count = 0
        i += 1

    sorted_dict = sorted(dict_w.items(), reverse=True, key=lambda x: x[1])  # Creates a sorted version of dict_w
    for value in sorted_dict:
        print(value[0], ":", value[1])     # Prints from the most frequent to least frequent word

    char_count = 0
    char_count_list = []
    alphabet = []
    char = []

    for word in text:
        char += word.split()  # Loops through the list of words and split each word into a set of characters

    for i in range(97,123):
        alphabet.append(chr(i))  # Loops through the list of lowercase characters in ASCII, adding them to a list

    # Nested loop that iterates through the alphabet
    for i in range(len(alphabet)):
        for k in range(len(char)):
            if alphabet[i] == char[k]:
                char_count += 1    # Adds one every time a letter appears

        char_count_list.insert(i, char_count)  # Inserts the character_count into a list
        char_count = 0

    for b in range(0, 26):
        print(alphabet[b], ": ", char_count_list[b])  # Prints each character to its respective frequency


count()   # Initializes the function

