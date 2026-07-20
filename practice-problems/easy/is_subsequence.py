# # Approach
# 1) Focus on order, not continuity.
# A subsequence only requires characters to appear in the same order—they do not need to be adjacent.

# 2) Track progress through the smaller string.
# Keep a pointer (cnt) that represents how many characters of s have been matched so far.

# 3) Scan the larger string once.
# Traverse t from left to right, advancing the pointer only when the current character matches the next required character in s.

# 4) Check if all characters were matched.
# If the pointer reaches the length of s, every character was found in order, so s is a subsequence of t.

# # Complexity
# - Time complexity:
# O(n) Where n -> len(t)

# - Space complexity:
# O(1)


# Code
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cnt = 0

        for i in range(len(t)):
            if cnt < len(s) and t[i] == s[cnt]:
                cnt += 1
                  
        return cnt == len(s)
