class Solution:
    def longestSubarray(self, nums) -> int:
        left = zero = length = 0


        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1

                left += 1
            
            length = max(length, right - left)

        return length


# 1. Expand the Window:
#    Move the right pointer forward and include the current element while counting the number of zeros in the window.

# 2. Maintain the Window:
#    Keep at most one zero in the current window, since one element can be deleted.

# 3. Shrink the Window:
#    If the window contains more than one zero, move the left pointer forward until only one zero remains.

# 4. Update the Answer:
#    After the window is valid, update the maximum subarray length as (right - left), which accounts for deleting one element.

# Time Complexity:
# O(n)
# - The left and right pointers each traverse the array at most once.

# Space Complexity:
# O(1)
# - Only a few variables (left, right, zero, length) are used, regardless of the input size.