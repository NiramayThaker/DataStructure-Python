# Apprach 1

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        mx_len = 0
        zero_cnt = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            
            mx_len = max(mx_len, right - left + 1)
        
        return mx_len

# 1. Expand the Window:
#    Move the right pointer forward and include the current element in the window.

# 2. Update the Window State:
#    Update the required information (e.g., count of zeros, frequency map, sum) based on the newly added element.

# 3. Shrink the Window:
#    While the window is invalid, move the left pointer forward and update the window state until it becomes valid again.

# 4. Update the Answer:
#    Once the window is valid, calculate the current window length and update the maximum answer.


# Approach - 2

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
            
            