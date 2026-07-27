class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = y = float("-inf")

        for i in nums:
            if i > x:
                y = x
                x = i
            elif i > y:
                y = i

        return (x - 1) * (y - 1)
    
    
# Approach 
# 1. Traverse the array once while maintaining the **largest** and **second largest** elements.
# 2. If the current element is greater than the largest, update the second largest to the old largest, then update the largest.
# 3. Otherwise, if the current element is greater than the second largest, update only the second largest.
# 4. Return the product `(largest - 1) * (second_largest - 1)`.
