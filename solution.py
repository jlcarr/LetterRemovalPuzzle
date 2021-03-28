"""
A small program to solve the following riddle:

What 8 letter word can have a letter taken away and it still makes a word.
Take another letter away and it still makes a word.
Keep on doing that until you have one letter left.
What is the word?
"""

# Read the wordlist used. The choice of wordlist greatly affects the solution
with open('wordlist.txt', 'r') as file:
	wordlist = file.read().lower().splitlines()
wordlist = set(wordlist)

# Parse wordlist is sets of words by length
max_len = max(map(len, wordlist))
len_sets = [set() for i in range(max_len+1)]
len_sets[0].add("")
for word in wordlist:
	len_sets[len(word)].add(word)
#print(f"Max word length: {max_len}")

# A depth-first search function
def search_function(word):
	if word == "":  # If we reach here we have a solution
		return []
	for i in range(len(word)):  # Try removing each letter
		new_word = word[:i]+word[i+1:]
		if new_word in len_sets[len(new_word)]:  # See if we have a valid word still
			rval = search_function(new_word)  # If we do continue the search
			if rval != None:  # If we found a solution return it
				return [word] + rval

# Solve the puzzle be seeing which 8 letter words produce solutions
puzzle_size = 8
for word in sorted(len_sets[puzzle_size]):
	result = search_function(word)
	if result:
		print(result)
