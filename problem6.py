# Problem 6. One of the best ways to improve as a Scrabble player is to learn
# all the 2 and 3 letter words.  It should be noted that many Scrabble players
# believe it is a waste of time (and brain power) to learn the definitions.
#
# Given a list of all the 3 letter Scrabble words (3letter_words.txt) you will
# write a program to sort the list by the highest scoring words.  The file is
# in the following format, where the 3 letter word is following by a space and
# then the definition:
#
#  AAH	to exclaim in delight
#  AAL	East Indian shrub
#  AAS	[aa] (rough, cindery lava)
#
# You should create a module named `words` that will handle all the functions
# related to reading, scoring and sorting the list.
#
# When you run the program, it should import the words module to read in the 3
# letter word list, compute the score for each word, and sort the words by
# descending score (i.e. highest scoring words to lowest scoring words).  Print
# the words out in sorted order to a file named 3letter_words_sorted.txt.  You
# do not need to print out the definitions.
#


# Use the following dictionary to look up the point value for each word.  A
# words total point value is the sum of points of each letter.
tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

# Problem 6. One of the best ways to improve as a Scrabble player is to learn
# all the 2 and 3 letter words.  It should be noted that many Scrabble players
# believe it is a waste of time (and brain power) to learn the definitions.
#
# Given a list of all the 3 letter Scrabble words (3letter_words.txt) you will
# write a program to sort the list by the highest scoring words.  The file is
# in the following format, where the 3 letter word is following by a space and
# then the definition:
#
#  AAH	to exclaim in delight
#  AAL	East Indian shrub
#  AAS	[aa] (rough, cindery lava)
#
# You should create a module named `words` that will handle all the functions
# related to reading, scoring and sorting the list.
#
# When you run the program, it should import the words module to read in the 3
# letter word list, compute the score for each word, and sort the words by
# descending score (i.e. highest scoring words to lowest scoring words).  Print
# the words out in sorted order to a file named 3letter_words_sorted.txt.  You
# do not need to print out the definitions.
#

# Use the following dictionary to look up the point value for each word.  A
# words total point value is the sum of points of each letter.
tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

import words
## more time implied would have correctly refactored code

# Problem 6. One of the best ways to improve as a Scrabble player is to learn
# all the 2 and 3 letter words.  It should be noted that many Scrabble players
# believe it is a waste of time (and brain power) to learn the definitions.
#
# Given a list of all the 3 letter Scrabble words (3letter_words.txt) you will
# write a program to sort the list by the highest scoring words.  The file is
# in the following format, where the 3 letter word is following by a space and
# then the definition:
#
#  AAH	to exclaim in delight
#  AAL	East Indian shrub
#  AAS	[aa] (rough, cindery lava)
#
# You should create a module named `words` that will handle all the functions
# related to reading, scoring and sorting the list.
#
# When you run the program, it should import the words module to read in the 3
# letter word list, compute the score for each word, and sort the words by
# descending score (i.e. highest scoring words to lowest scoring words).  Print
# the words out in sorted order to a file named 3letter_words_sorted.txt.  You
# do not need to print out the definitions.
#

# Use the following dictionary to look up the point value for each word.  A
# words total point value is the sum of points of each letter.

tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
points = []
all_words_list = []
all_scores = {}
#Read data

def reader(filename):
    flatten_list = []
    fc = open(filename, 'r')
    for line in fc:
        # Remove whitespace and append to list
        # Change case
        line = line.lower()
        # Homogenize tabs and new line characters
        line = line.replace('\t',' ')
        line = line.replace('\n',' ')
        line.strip()
        # Create a list with words
        clean_words = line.split(' ')
        all_words_list.append(clean_words[:1])
    fc.close()
    # clean up with only scrabble words
    flatten_list = sum(all_words_list, [])
#    print flatten_list
    points = 0
    point_calc = []
    words_points = []
# assign points
# Getting an error here -- else able to correctly parse flatten_list
    for i in range(len(flatten_list)):
        points = 0
        str1 = flatten_list[i][0]
        str2 = flatten_list[i][1]
        str3 = flatten_list[i][2]
        print str1
        points = tile_score[str1]+tile_score[str2]+tile_score[str3]
        words_points.append([i, points])
        points = 0

# sort by points  --- sorting multidimensional array using lambda function -- exactly same as HW 3
    sorted_unique_words = []
    sorted_unique_words = sorted(unique_words_list,key=lambda x: x[1], reverse = True)
    return sorted_unique_words

# writing to file -- super easy!
def writer(sorted_unique_words):
    dataset = []
    f = open("3_letter_words_sorted.txt", 'w')
    for i in len(sorted_unique_words):
        f.write(sorted_unique_words[i])
        f.write("\n")
    f.close()


lister = []
kk = []

lister = reader("3letter_words.txt")
kk = point_assigner_sort(lister)
writer(kk)
