# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    if (len(word1) == len(word2)):
        word1 = sorted(word1)
        word2 = sorted(word2)
        if word1 == word2:
         return True
        else:
            return False 
print(find_anagrams("rear", "rare"))

