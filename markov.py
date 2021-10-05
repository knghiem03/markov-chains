"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_text = open(file_path).read()
    return full_text

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    #make a for loop that returns all two-word pieces of the text

    i=0
    word_list = text_string.split()
    word_list.append(None)
    while i <= len(word_list)-3:
        bigram = (word_list[i], word_list[i+1])

        if bigram in chains.keys():
            #print(word_list[i+2])
            #if chains[bigram]:
            #print("helllo 2222 ")
            chains[bigram].append(word_list[i+2])
        else:
            #print(word_list[i+2])
            #print(f"{bigram} --- {word_list[i+2]}")
            chains[bigram] = [word_list[i+2]]
        i += 1
    #for key in chains.keys():
    #   print(f"{key}--------{chains[key]}")
    return chains

def make_text(chains):
    """Return text from chains."""
    words = []
    first_key = ('could', 'you')
        
    while True:
        if first_key in chains.keys():
            random_value = choice(list(chains[first_key]))
            words.append(first_key[0])
            words.append(first_key[1])
            first_key = ( first_key[1], random_value )
            print(f"key and random word {first_key} --- {random_value}")
            words.append(random_value)
        else:
            break

    print(f"Words list : {words}")
    #return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

