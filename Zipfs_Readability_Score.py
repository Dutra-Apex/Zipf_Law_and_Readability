"""
04/01/2020

Program: Zipfs_Readability_Score
Written by: Gabriel Dutra

The code's main goal is to utilize the slope of a Zipfian distribution from a given text to analyze and quantify
the text's complexity through the metric of Flesch's Readability Scores.
"""

import matplotlib.pyplot as plt
import math
import numpy as np
import textatistic

# Prints the Zipfian distribution of a text
def zipf(text):
    file = open(text, "rt", encoding="UTF-8") # Opens file with proper encoding
    text = (file.read()).lower()
    file.close()

    # Replaces any character that can interfer with the word frequency distribution
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace("'", "")
    text = text.replace(" \" ", "")
    text = text.replace("-", "")
    text = text.replace("—", "")
    text = text.replace(";", "")
    text = text.replace("\n", "")
    
    # Splits the text into words, putting them into a list
    words = text.split()
    word_count = 0
    dict_w = {}

    # Loops through the list, counts their frequency and  creates a dictionary (dict_w) that contains each word with their number of occurences
    for i in range(len(words)):
        for j in words:
            if j == words[i]:
                word_count += 1
        dict_w[words[i]] = word_count
        word_count = 0
        i += 1

    # Sorts the dictionary from the most frequent word to the least frequent
    sorted_dict = sorted(dict_w.items(), reverse=True, key=lambda x: x[1])
    word_list = []
    count_list = []

    for x, y in sorted_dict:
        word_list.append(x)
        count_list.append(y)

    rank_list = []

    # Creates a list containing the log of the word's occurance and rank
    for i in range(0, len(count_list)):
        count_list[i] = math.log(count_list[i], 10)
        rank_list.append(math.log(i+1, 10))

    # Initializes the log of the list of ranks and the log of the list of frequencies as numpy arrays for future use
    rank_list = np.array(rank_list)
    count_list = np.array(count_list)

    #Equations for line of best fit
    denominator = rank_list.dot(rank_list) - rank_list.mean() * rank_list.sum()
    m = (rank_list.dot(count_list) - count_list.mean() * rank_list.sum()) / denominator
    b = (count_list.mean() * rank_list.dot(rank_list) - rank_list.mean() * rank_list.dot(count_list)) / denominator
    best_fit = m * rank_list + b

    residual = count_list - best_fit
    total = count_list - count_list.mean()
    r_squared = 1 - residual.dot(residual) / total.dot(total)    
    
    # Prints the result
    print("The R^2 is: ", r_squared)
    print("The slope is: ", m)

    # Prints the distribution of words and their ranks
    plt.scatter(word_list, count_list)
    plt.ylabel("Word frequency")
    plt.xlabel("Word rank")
    plt.title("Frequency vs Rank")
    plt.show()

    # Prints the logged graph of the zipfian distribution
    plt.scatter(rank_list,count_list, s=1)
    plt.plot(rank_list, best_fit, color="red")
    plt.ylabel("Word frequency (logged)")
    plt.xlabel("Word rank (logged)")
    plt.title("log(frequency) vs log(rank)")
    plt.show()


# Function that prints the readability score of a given text
def reading_ease(txt):
    file = open(txt, "rt", encoding="UTF-8")
    text = (file.read()).lower()
    file.close()
    print()
    print(txt)
    print("The readability score is: ",textatistic.flesch_score(text))  #Uses the library textatistic, which contains dictionaries from PyHyphen

# Call functions by using any sample text encoded in UTF-8
zipf("sample.txt")
reading_ease("sample.txt")
