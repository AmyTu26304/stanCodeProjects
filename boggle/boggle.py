"""
File: boggle.py
Name: Yi-Chen Tu (Amy Tu)
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():

	s_dict = {}
	for i in range(1, 5):
		r = input(f"{i} row of letters: ").lower()
		lst_r = r.split(" ")
		if len(lst_r) != 4 or len(r) != 7:
			print("Illegal input")
			break
		for j in range(1, 5):
			s_dict[(j, i)] = lst_r[j-1]
	start = time.time()
	####################
	print("There are", len(find_word(s_dict)), "words in total.")
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = {}
	with open(FILE, "r") as f:
		for line in f:
			if line[0] not in dic:
				dic[line[0]] = [line.strip()]
			else:
				dic[line[0]].append(line.strip())
	return dic


def find_word(s_dict: dict) -> list:
	all_words = []
	d = read_dictionary()
	for key, value in s_dict.items():
		cur_s = s_dict[key]
		looped = [key, ]
		find_word_helper(s_dict, cur_s, key, looped, all_words, d)
	return all_words


def find_word_helper(s_dict: dict, cur_s: str, key: tuple, looped: list, all_words: list, d: dict) -> list:
	if len(looped) == 6:
		return all_words
	else:			# find neighbors
		x = key[0]
		y = key[1]
		for i in range(-1, 2):
			for j in range(-1, 2):
				x1 = x + i  # get adjacent characters
				y1 = y + j
				if (x1, y1) in s_dict and (x1, y1) not in looped:
					# Choose
					neighbor = s_dict[(x1, y1)]
					cur_s += neighbor
					key = (x1, y1)
					looped.append((x1, y1))

					if len(cur_s) >= 4:
						if cur_s in d[cur_s[0]] and cur_s not in all_words:
							print(f'Found: "{cur_s}"')
							all_words.append(cur_s)

					if len(cur_s) == 1 or (len(cur_s) > 1 and has_prefix(cur_s, d)):
						# Explore
						find_word_helper(s_dict, cur_s, key, looped, all_words, d)

					# Un-choose
					cur_s = cur_s[:-1]
					looped.remove((x1, y1))

	return all_words


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param d: (list)
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
