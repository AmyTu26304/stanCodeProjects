"""
File: anagram_ext.py
Name: Yi-Chen Tu (Amy Tu)
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: This program recursively finds all the anagram(s)
          for the word input by user and terminates when the
          input string matches the EXIT constant
    """

    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        s = input("Find anagrams for: ")
        start = time.time()
        ####################
        if s == EXIT:
            break
        print("Searching...")
        new_dict = new_dictionary(s)
        anagrams_lst = []
        for word in new_dict:
            if find_anagrams(list(s), list(word)):
                print("Found:", word)
                print("Searching...")
                anagrams_lst.append(word)
        print(len(anagrams_lst), "anagrams:", anagrams_lst)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def new_dictionary(s):
    """
    :param s: str, word to search for anagrams
    :return: new_dict: lst, a dictionary containing words in same length of s
    """
    lst = []
    with open(FILE, "r") as f:
        for line in f:
            if len(line) == len(s)+1:
                # lst contains words in same length of len(s)
                lst.append(line.strip())
    return lst


def find_anagrams(s, word):
    """
    :param s: lst, input word to search for anagrams
    :param word: lst, word to search in new_dict
    :return: boolean, if word is an anagram of s or not
    """
    # Base case
    if s == word == []:
        return True             # if characters of s matches those of word, regardless of the order
    else:
        for ch in s:
            if ch in word:
                # pop the same character from s and word
                i = s.index(ch)
                s.pop(i)
                j = word.index(ch)
                word.pop(j)
                return find_anagrams(s, word)
            else:
                return False    # mismatch of character


if __name__ == '__main__':
    main()
