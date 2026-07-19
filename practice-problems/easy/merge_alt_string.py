class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alt_str:str = ""
        w1_len, w2_len = len(word1), len(word2)
        itr = min(w1_len, w2_len)

        for i in range(itr):
            alt_str += (word1[i] + word2[i])
        
        if w1_len > itr:
            alt_str += word1[itr:]
        elif w2_len > itr:
            alt_str += word2[itr:]

        return alt_str


#1) Focus on the common part first.
# Since characters are merged alternately, iterate only until the length of the shorter string.
 
# 2) Process both strings together.
# At each index, append one character from word1 followed by one from word2 to maintain the alternating order.

# 3) Handle the leftover separately.
# After the common portion is processed, only one string can have remaining characters—append them directly.

# 4) Break the problem into two phases.
# Phase 1: Alternate characters while both strings have characters.
# Phase 2: Append the remaining suffix from the longer string.