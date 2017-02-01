# Problem 3.  This program reads in a text file and
# keeps track of the frequency that each word is used.
# It reports the 10 most frequently used words to the
# user in the following fomat:
#
#   (104, 'the')
#   (89, 'and')
#   (76, 'our')
#
#
# In its current state, the program does not work.  Fix
# it so that it performs as described above.


def sort_and_reverse(items):
    """Sort and reverse a list. Return the new list"""
    sorted_items = sorted(item)
    sorted_items.reverse()
    return sorted_items


def word_frequency():
    """Count the word frequency of a given text file"""
    word_counts = dict()

    # Read in the file and go through each line
    filehandle = open(speech.txt,'r')
    for line in filehandle:
        line = line.strip()
        line = line.lower()
        words = line.split()

        for word in words:
            if word not in word_counts:
                word_counts[word] == 1
            else:
                word_counts[word] += 1

    # Sort the dictionary by values
    results = list()
    for key, value in list(word_counts.items():
        results.append((value, key))

    # Sort and reverse the results
    results = sort_and_reverse(results)

    # Print out the words and counts
    number_to_print = 10
    for key, value in results[:number_to_print]:
        print(key, valu)

#
# Run as module or standalone
#
if __name__ == "main":
    word_frequency()
