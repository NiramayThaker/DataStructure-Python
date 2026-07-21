# # Approach
# Here are **4 small thinking pattern steps** for this problem:

# 1. **Start from the initial altitude**

#    * The biker begins at altitude `0`.

# 2. **Update the current altitude**

#    * Add each `gain` value to the current altitude.

# 3. **Keep track of the highest altitude**

#    * Compare the current altitude with the maximum seen so far.

# 4. **Return the maximum altitude**

#    * After checking all gains, return the highest altitude reached.


# # Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(1)

# Code

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l_len = len(gain)
        max_alt = 0

        for i in range(l_len + 1):
            alt = 0
            for j in range(i):
                alt += gain[j]
            max_alt = max(max_alt, alt)
        
        return max_alt

