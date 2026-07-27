# Approach - 1:
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = []
        count2 = []

        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        for i in range(97, 123):
            char = chr(i)
            count1.append(word1.count(char))
            count2.append(word2.count(char))

        return sorted(count1) == sorted(count2)


# 1. Check if both strings have the same length and contain the same set of characters. If not, return False.
# 2. Create two frequency arrays of size 26 to store the occurrence count of each lowercase character.
# 3. Iterate through all possible characters ('a' to 'z') and store their frequencies for both words.
# 4. Sort both frequency arrays and compare them. If they are equal, both strings have the same frequency distribution and are close strings.

# Time Complexity: O(n + k log k)
# - n is the length of the string.
# - k is the number of possible characters (26).
# - Counting characters takes O(n), and sorting the frequency arrays takes O(26 log 26), which is constant.

# Space Complexity: O(1)
# - Uses two fixed-size arrays of size 26, independent of input size.


# Approach - 2
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        w1_occ = {}
        w2_occ = {}

        for ch in word1:
            w1_occ[ch] = w1_occ.get(ch, 0) + 1

        for ch in word2:
            w2_occ[ch] = w2_occ.get(ch, 0) + 1

        return sorted(w1_occ.values()) == sorted(w2_occ.values())


# 1. Check if both strings have the same length and contain the same set of characters. If not, return False.
# 2. Use hash maps to count the frequency of each character in both strings.
# 3. Compare the sorted list of frequency values from both hash maps.
# 4. If both frequency distributions match, the strings are close strings.

# Time Complexity: O(n + k log k)
# - n is the length of the string.
# - k is the number of unique characters.
# - Creating frequency maps takes O(n), and sorting frequency values takes O(k log k).

# Space Complexity: O(k)
# - Stores the frequency of each unique character in hash maps.
# - k represents the number of unique characters in the string.