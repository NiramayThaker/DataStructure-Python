# Intuition
# Approach

# 1. **Each answer is the product of all elements to the left × all elements to the right of the current index.**

# 2. **Compute and store prefix (left) products in the output array during the first pass.**

# 3. **Traverse from right to left while maintaining a running suffix (right) product.**

# 4. **Multiply the stored prefix product by the current suffix product to get the final answer in O(n) time and O(1) extra space.**


# Code
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix_product = 1
        postfix_product = 1
        result = [0] * n

        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result
