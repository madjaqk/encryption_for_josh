import datetime
import itertools

def numberfy(string):
    # Returns a list with the unicode values of the letters in a string
    return [ord(c) for c in string]

def letterfy(num_list):
    # Converts a list of unicode values (such as produced by numberfy) into a
    # string
    return "".join([chr(i) for i in num_list])

def encrypt(string, key):
    num_list = numberfy(string)
    key = numberfy(key)

    # As in a Vigenère cipher, shifts each letter in the message forward by the
    # based on the corresponding character in the key.  itertools.cycle()
    # returns an endless series, so there's no chance of the key being too short
    output = [x[0] + x[1] for x in zip(num_list, itertools.cycle(key))]
    output = letterfy(output)

    return output

def decrypt(string, key):
    num_list = numberfy(string)
    key = numberfy(key)

    # Undoes the Vigenère cipher
    output = [x[0] - x[1] for x in zip(num_list, itertools.cycle(key))]
    output = letterfy(output)

    return output

# datetime.datetime.now() returns a never-before-used key
timecode = str(datetime.datetime.now())

pride_and_prejudice = 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. "My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?" Mr. Bennet replied that he had not. "But it is," returned she; "for Mrs. Long has just been here, and she told me all about it." Mr. Bennet made no answer. "Do you not want to know who has taken it?" cried his wife impatiently. "You want to tell me, and I have no objection to hearing it." This was invitation enough.'

secret = encrypt(pride_and_prejudice, timecode)

print(secret)
print("")
print(decrypt(secret, timecode))
print("")

"""
One problem with this is that, as you probably noticed, many of the characters
in encrypted string are unprintable, so the message appears rather than shorter
than it should.  One alternative would be to use a list containing all printable
characters instead of the unicode character set.
"""

import numbers
import re

def alt_numberfy(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890"
    return [letters.find(c) if c in letters else c for c in string]

def alt_letterfy(num_list):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890"
    return "".join([letters[i] if isinstance(i, numbers.Number) else i for i in num_list])

def alt_encrypt(string, key):
    num_list = alt_numberfy(string)
    key = alt_numberfy(key)

    output = [(x[0] + x[1]) % 63 if isinstance(x[0], numbers.Number) else x[0] for x in zip(num_list, itertools.cycle(key))]
    output = alt_letterfy(output)

    return output

def alt_decrypt(string, key):
    num_list = alt_numberfy(string)
    key = alt_numberfy(key)

    # Undoes the Vigenère cipher
    output = [(x[0] - x[1]) % 63 if isinstance(x[0], numbers.Number) else x[0] for x in zip(num_list, itertools.cycle(key))]
    output = alt_letterfy(output)

    return output

regex = re.compile(r"[^a-zA-z0-9]")
timecode = str(datetime.datetime.now())
timecode = regex.sub("", timecode)
secret = alt_encrypt(pride_and_prejudice, timecode)

print(secret)
print("")
print(alt_decrypt(secret, timecode))
print("")


