"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
# start time 8:31pm end time 10:16pm
#start time 1pm-2pm

def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    #made a set out of the list to remove dups
    word_set = set(words)

    # cast the set to a list so that a list would be returned
    return list(word_set)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    #converted each list into sets
    set1 = set(items1)
    set2 = set(items2)

    #made new set of the intersection of the 2 sets
    unique_items = set1 & set2

    #cast the set to a list
    return list(unique_items)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    #empty dictionary
    word_count = {}

    #loop through the each word in the phrase
    for word in phrase.split():
        # if the word is already in the dictionary the add 1
        if word_count.has_key(word):
            word_count[word] = word_count[word] + 1
        #if the word is not in the dictionary, add it
        else:
            word_count[word] = 1

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    #made pirate to english dictionary
    pirate_talk = { 'sir': 'matey',
                    'hotel': 'fleabag inn',
                    'student': 'swabbie',
                    'boy': 'matey',
                    'professor': 'foul blaggart',
                    'restaurant': 'galley',
                    'your': 'yer',
                    'excuse': 'arr',
                    'students': 'swabbies',
                    'are': 'be',
                    'restroom': 'head',
                    'my': 'me',
                    'is': 'be',
                    'man': 'matey',}
    # creates a list of words from phrase
    phrase_tokens = phrase.split()
    
    #enumerated over the list of words to get index and value
    for index, word in enumerate(phrase_tokens):
        #checked to see if the word was in the dictionary
        if pirate_talk.has_key(word):
            #if found i would replace the english word for the pirate one
            phrase_tokens[index] = pirate_talk[word]
        #not in the dict. the english word would stay
        else: 
            phrase_tokens[index] = word

            #returned a new string based on the changed list
    return " ".join(phrase_tokens)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    #empty dictionary
    word_length = {}

    #loop through the words list
    for each_word in words:
        #check to see if dictionary already has an entry for size of word
        if word_length.has_key(len(each_word)):
            #yes, then append new word to value list
            word_length[len(each_word)].append(each_word)
        #no, then create new key:value pair
        else:
            word_length[len(each_word)] = [each_word,]
    
            #return dictionary as a list of key:value pairs
    return word_length.items()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    #empty set
    zero_pairs = set()
    #loop through numbers list
    for number in numbers:
        #second loop adds each number to the number from outter loop
        #ie. numbers = [1,2,3]. pattern: 1+1,1+2,1+3 then 2+1,2+2,2+3 etc
        for idx in range(len(numbers)):
            if number + numbers[idx] == 0:
                #first sorted a list of 2 numbers
                #then cast as a tuple (since sets cant take lists)
                #add the tuple to the set, if dup, set ignores
                zero_pairs.add(tuple(sorted([number, numbers[idx]])) )
            else:
                continue
    #returned the set cast as a list as per requirements
    return list(zero_pairs)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #dictionary where key is a name and value is a list of other names that 
    #start with the last letter of the key
    name_dict = {}
    
    # loop to populate the dictionary
    for name in names:
        #finds the last letter of the name that will be used as a key
        last_letter = name[-1]
        
        # list to hold names who's first letter matches 
        # the last letter of the key
        temp = []
        
        # name[1:] is to make sure the first name in names list does not get
        # added to the dictionary
        for item in names[1:]:
            #checks to see if the last 
            if last_letter == item[0]:
                #if match found appends to the temp list
                temp.append(item)
            else:
                continue
        # after looking through names adds name as the key and 
        # temp list as the value to the dictionary
        name_dict[name] = temp

    # creat a new list to hold the correct chain of names
    new_list = [names[0]]

    #loops as long as the value of the key is not and empty list
    while name_dict[new_list[-1]] != []:

        #temp var to hold the popped off item
        #pop removes the item from the value list so we dont select it again
        item = name_dict[new_list[-1]].pop(0)
        # if the item is not in the list, append it
        if not item in new_list:
            new_list.append(item)
        
        #otherwise go through the loop again
        else:
            continue
        # print "new list is", new_list

    #returns the newly generated list
    return new_list


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print