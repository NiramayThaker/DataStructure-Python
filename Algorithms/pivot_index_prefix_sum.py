# Approach

# 1. **Understand the starting point** – Identify the initial state (altitude starts at `0`).
# 2. **Maintain a running value** – Update the current altitude after each gain/loss.
# 3. **Track the best answer** – Continuously store the maximum altitude seen so far.
# 4. **Return the final result** – After one complete traversal, return the maximum altitude.

# This is a common pattern: **Initialize → Update → Compare → Return**.

# Code
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum == sum(nums[i:]):
                return i
        
        return -1
