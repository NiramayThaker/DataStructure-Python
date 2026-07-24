# # Approach

# 1. **Initialize two pointers** at the beginning (`left`) and end (`right`) of the array to maximize the initial container width.
# 2. **Calculate the current area** using `min(height[left], height[right]) × (right - left)` and update the maximum area found.
# 3. **Move the pointer with the smaller height** inward, as the shorter line limits the current container's height; moving the taller line cannot increase the area.
# 4. **Repeat until both pointers meet**, ensuring all potential maximum-area containers are evaluated efficiently.

# ### **Complexity**

# * **Time Complexity:** **O(n)** — Each pointer moves at most `n` times, so the array is traversed once.
# * **Space Complexity:** **O(1)** — Only a few extra variables are used, regardless of the input size.

## MAX AREA PROBLEM

# Code
class Solution:
    def maxArea(self, height) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            width = right - left
            current_area = min(height[left], height[right]) * width

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
