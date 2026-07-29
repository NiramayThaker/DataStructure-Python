class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = {}
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


# Approach (4 Steps)

# 1. Initialize the Sliding Window:
#    Maintain two pointers (`left` and `right`) to represent the current substring without repeating characters. Use a hash map to store the most recent index of each character and initialize a variable to track the maximum substring length.

# 2. Expand the Window:
#    Traverse the string by moving the `right` pointer one character at a time. For each character, check whether it has already appeared in the current sliding window.

# 3. Adjust the Window:
#    If a duplicate character is found within the current window, move the `left` pointer to the position immediately after the character's previous occurrence. This ensures the window always contains unique characters.

# 4. Update the Result:
#    After each iteration, calculate the length of the current valid window and update the maximum length if the current window is longer. Continue until the entire string has been processed, then return the maximum length found.
