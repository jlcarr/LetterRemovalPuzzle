# LetterRemovalPuzzle
A Python script to solve a word puzzle.

## Puzzle Definition
What 8 letter word can have a letter taken away and it still makes a word. 
Take another letter away and it still makes a word. 
Keep on doing that until you have one letter left. 
What is the word?

## Solution Approach
### Solving By Hand
First thing to think about is what 1-letter words are there? Really only 2 proper ones:  
- *A*
- *I*

Now what 2-letter words can be built up? For strictly proper words, omitting all short-forms and slang, the list is again quite short:  
- *AH*
- *AM*
- *AN*
- *AS*
- *AT*
- *IF*
- *IN*
- *IS*
- *IT*
This is ommitting words like *MA*, *PA*, *HA* and *YA*, but we should keep those in mind too.

Next a good strategy is to look at suffixes that can be whittled down to other valid suffixes, e.g.:  
*ERS* -> *ER* -> *E*  
*INGS* -> *ING* -> *IN*  

Using these strategies I managed to come up with the following solution:
**MANAGERS** -> *MANAGER* -> *MANAGE* -> *MANGE* -> *MANE* -> *MAN* -> *AN* -> *A*

Though the popular solution found on the internet is:
**STARTING** -> *STARING* -> *STRING* -> *STING* -> *SING* -> *SIN* -> *IN* -> *I*

### Solving Programmatically
The solution can of course be solved programmatically with a simple search algorithm and a wordlist.  
**NOTE**: The solutions can vary greatly by what the wordlist considers to be real words.  
I implemented a solving algorithm in Python to find all words that result in solutions (though it only return 1 possible solution for each valid starting word).  
Here's the result from the wordlist I found worked best:
```
['ashtrays', 'ashtray', 'astray', 'stray', 'tray', 'ray', 'ay', 'a']
['bearings', 'bearing', 'baring', 'bring', 'ring', 'rin', 'in', 'i']
['bragging', 'ragging', 'raging', 'aging', 'agin', 'gin', 'in', 'i']
['cheaters', 'cheater', 'heater', 'hater', 'hate', 'ate', 'at', 'a']
['cleansed', 'cleanse', 'cleans', 'clean', 'clan', 'can', 'an', 'a']
['cleanser', 'cleanse', 'cleans', 'clean', 'clan', 'can', 'an', 'a']
['cleanses', 'cleanse', 'cleans', 'clean', 'clan', 'can', 'an', 'a']
['cremated', 'created', 'crated', 'rated', 'rate', 'ate', 'at', 'a']
['crowding', 'crowing', 'rowing', 'owing', 'wing', 'win', 'in', 'i']
['crowning', 'crowing', 'rowing', 'owing', 'wing', 'win', 'in', 'i']
['dragging', 'ragging', 'raging', 'aging', 'agin', 'gin', 'in', 'i']
['drowning', 'downing', 'owning', 'owing', 'wing', 'win', 'in', 'i']
['failings', 'failing', 'filing', 'fling', 'ling', 'lin', 'in', 'i']
['fillings', 'filling', 'filing', 'fling', 'ling', 'lin', 'in', 'i']
['flailing', 'failing', 'filing', 'fling', 'ling', 'lin', 'in', 'i']
['flatters', 'flatter', 'latter', 'later', 'late', 'ate', 'at', 'a']
['flattery', 'flatter', 'latter', 'later', 'late', 'ate', 'at', 'a']
['platters', 'platter', 'latter', 'later', 'late', 'ate', 'at', 'a']
['pointers', 'pointer', 'pointe', 'point', 'pint', 'pit', 'it', 'i']
['shingles', 'singles', 'single', 'singe', 'sine', 'sin', 'in', 'i']
['splatter', 'platter', 'latter', 'later', 'late', 'ate', 'at', 'a']
['stalkers', 'stalker', 'talker', 'taker', 'take', 'tae', 'ta', 'a']
['starling', 'staring', 'string', 'sting', 'ting', 'tin', 'in', 'i']
['starring', 'staring', 'string', 'sting', 'ting', 'tin', 'in', 'i']
['starting', 'staring', 'string', 'sting', 'ting', 'tin', 'in', 'i']
['startled', 'started', 'stated', 'state', 'tate', 'ate', 'at', 'a']
['starving', 'staring', 'string', 'sting', 'ting', 'tin', 'in', 'i']
['statutes', 'statues', 'states', 'stats', 'stat', 'tat', 'at', 'a']
['storming', 'storing', 'string', 'sting', 'ting', 'tin', 'in', 'i']
['strapped', 'trapped', 'tapped', 'taped', 'tape', 'tae', 'ta', 'a']
['stripped', 'striped', 'stripe', 'tripe', 'trip', 'tip', 'ti', 'i']
['swingers', 'singers', 'singer', 'singe', 'sine', 'sin', 'in', 'i']
['theaters', 'theater', 'heater', 'hater', 'hate', 'ate', 'at', 'a']
```
Interestingly *MANAGERS* wasn't among its solutions because neither *MANE* nor *MANGE* were in the wordlist! Go figure!
