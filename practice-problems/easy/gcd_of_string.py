class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1
        
        return str1[:gcd(len(str1), len(str2))]



# Approch

# 1) Look for mathematical clues.
# Keywords like "greatest", "common", and "divides" often hint that a 
# GCD (Greatest Common Divisor) approach might simplify the problem.

# 2) Validate the repeating pattern first.
# Before finding the answer, check whether str1 + str2 == str2 + str1. If this fails, the strings cannot share a common divisor string.

# 3) Reduce the problem from strings to lengths.
# Once both strings share the same repeating pattern, the largest common divisor string must have a length equal to gcd(len(str1), len(str2)).

# 4) Use the prefix as the answer.
# After finding the GCD of the lengths, simply return the first gcd_length characters of either string—they represent the largest repeating unit shared by both strings.
