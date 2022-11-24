"""
File: anagram.py
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
        anagrams_lst = find_anagrams(s)
        print(len(anagrams_lst), "anagrams:", anagrams_lst)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    lst = []
    with open(FILE, "r") as f:
        for line in f:
            lst.append(line.strip())
    return lst


def new_dictionary(s):
    """
    :param s: str, word to search for anagrams
    :return: new_dict: lst, a dictionary containing words in same length and characters of s
    """
    new_dict = []
    for word in read_dictionary():
        switch = True
        if len(word) == len(s):  # new_dict contains words in same length of len(s)
            for ch in word:
                if ch not in s:
                    switch = False
                    break
            if switch:           # all of the characters in word of new_dict is in s
                new_dict.append(word)
    return new_dict


def find_anagrams(s):
    """
    :param s: str, word to search for anagrams
    :return: lst, all anagrams of s
    """
    # characters of s is converted to indices
    # s_index = []
    # for i in range(len(s)):
    #     s_index.append(i)
    return find_anagrams_helper(s, [], list(s), [], new_dictionary(s))    # list of anagrams


def find_anagrams_helper(s, cur, s_remain, all_words, new_dict):
    """
    :param s: str, the input word
    :param cur: lst, the permutation of characters
    :param s_remain: lst, the remaining characters
    :param all_words: lst, all anagrams of s
    :param new_dict: lst, a dictionary containing words in same length and characters of s
    :return: lst, all anagrams of s
    """
    if len(s_remain) == 0:
        cur_s = "".join(cur)
        if cur_s in new_dict:  # cur_s is found in new dictionary
            if cur_s not in all_words:
                all_words.append(cur_s)
                print("Found:", cur_s)
                print("Searching...")

    else:
        for i in range(len(s_remain)):
            # Choose
            ch = s_remain.pop(i)
            cur.append(ch)
            # Explore
            find_anagrams_helper(s, cur, s_remain, all_words, new_dict)
            # Un-choose
            cur.pop()
            s_remain.insert(i, ch)
    return all_words                                                     # list of all possible anagrams


def has_prefix(all_words, new_dict):
    """
    :param all_words: lst, all possible anagrams
    :param new_dict: lst, a dictionary containing words in same length and characters of s
    :return: lst, all possible anagrams with prefix of the first two characters in dictionary
    """
    """
    new_all_words = []
    sub_s = " "
    for word in all_words:
        if word.startswith(sub_s):
            new_all_words.append(word)
        else:
            for new_dict_word in new_dict:
                if word.startswith(new_dict_word[:2]):
                    sub_s = new_dict_word[:2]
                    new_all_words.append(word)
                    break

    return new_all_words
    """


if __name__ == '__main__':
    main()
