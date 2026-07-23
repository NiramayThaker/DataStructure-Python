# Approach
# **Thinking Pattern:**

# 1. Sort the array so the lexicographically smallest and largest strings become the first and last elements.
# 2. Compare only the first and last strings, since any common prefix of all strings must exist between these two.
# 3. Traverse both strings character by character until a mismatch occurs or the shorter string ends.
# 4. Append matching characters to the answer and return the constructed longest common prefix.

# **Time Complexity:** `O(N log N + M)`

# * `N` = number of strings, `M` = length of the shortest string (comparison between first and last).

# **Space Complexity:** `O(1)` (excluding the output string)


# Code
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)

        first_ele = strs[0]
        last_ele = strs[-1]

        itr_n = min(len(first_ele), len(last_ele))

        for i in range(itr_n):
            
            if first_ele[i] != last_ele[i]:
                return ans

            ans += first_ele[i]
            
        return ans
