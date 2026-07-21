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
        current = 0
        best = 0

        for value in gain:
            current += value
            best = max(best, current)

        return best
