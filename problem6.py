# Problem 6. One of the best ways to improve as a Scrabble player is to learn
# all the 2 and 3 letter words.  It should be noted that many Scrabble players
# believe it is a waste of time (and brain power) to learn the definitions.
#
# Given a list of all the 3 letter Scrabble words (3letter_words.txt) you will
# write a program to sort the list by the highest scoring words.
#
# You should create a module named `words` that will handle all the functions
# related to reading, scoring and sorting the list.
#
# When you run the program, it should import the words module to read in the 3
# letter word list, compute the score for each word, and sort the words by
# descending score (i.e. highest scoring words to lowest scoring words).  Print
# the words out in sorted order to a file named 3letter_words_sorted.txt.
#


# Use the following dictionary to look up the point value for each word.  A
# words total point value is the sum of points of each letter.
tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
