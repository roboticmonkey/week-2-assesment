"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
#start time 2pm-2:15pm


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    #create empty dictionary to hold data
    char_dict = {}

    #loop through phrase adding characters to dict and increament their totals
    for char in phrase:
        if char != " ":
            if char_dict.has_key(char):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        else:
            continue
    
    #create empty vars. 
    highest_char = []
    highest_num = 0

    #loop through char_dict checking for highest number
    for item in char_dict.iteritems():
        # first time through set item to the highest char & num 
        if highest_char == []:
            highest_char = [item[0]]
            highest_num = item[1]
        
        # after first loop
        # if next item has a higher number replace the temp vars to be the 
        # highest
        elif item[1] > highest_num:
            highest_char = [item[0]]
            highest_num = item[1]
        # however if there is a matching high number, add new letter to the 
        # highest_char list
        elif item[1] == highest_num:
            highest_char.append(item[0])
        
        else:
            continue 

    # return a sorted list of characters
    return sorted(highest_char)


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    #empty dictionary
    word_length = {}

    #loop through the words list
    for each_word in words:
        #check to see if dictionary already has an entry for size of word
        if word_length.has_key(len(each_word)):
            #yes, then append new word to value list
            word_length[len(each_word)].append(each_word)
            #sort the value list and re-bid it to the key
            word_length[len(each_word)].sort()
        #no, then create new key:value pair
        else:
            word_length[len(each_word)] = [each_word,]
    
     
            #return dictionary as a sorted list of key:value pairs tuples
    return sorted(word_length.items())

    


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
