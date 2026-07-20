# Approach
# 1) Recognize the fixed-size window.
#   Since the subarray size k never changes, think Sliding Window instead of checking every possible subarray.

# 2) Compute the first window once.
#   Calculate the sum of the first k elements to establish the initial window.

# 3) Slide the window efficiently.
#   Instead of recalculating the entire sum, remove the outgoing element and add the incoming element to update the window in O(1) time.

# 4) Track the best result continuously.
#   After every window update, compare the current window sum with the maximum seen so far and update it if needed.

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(1)


# Code
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            # Reusing old value instead of calculating all the values
            # Windowm_sum = sum - 1_old_value + 1_upcoming_new_value
            window_sum = (window_sum - nums[i - k] + nums[i])
            if max_sum < window_sum:
                max_sum = window_sum
            
        return max_sum / k