class Solution:
    def maxOperations(self, nums, k) -> int:

        nums.sort()

        left = 0
        right = len(nums) - 1
        cnt = 0

        while left < right:

            su = nums[left] + nums[right]

            if su == k:
                cnt += 1
                left += 1
                right -= 1

            elif su > k:
                right -= 1

            else:
                left += 1

        return cnt

"""
Approach

Sort the array so that the smallest and largest values can be compared efficiently using two pointers.
Initialize two pointers (left at the beginning and right at the end) to explore possible pairs.
Adjust pointers based on the sum: if the current sum is greater than k, decrease the larger value; if the sum is smaller, increase the smaller value.
When a valid pair is found, increment the count and move both pointers to ensure each element is used only once.

Complexity

Time Complexity: O(n log n) — Sorting takes O(n log n), and the two-pointer traversal takes O(n).
Space Complexity: O(1) — Only constant extra variables are used (ignoring sorting space).
"""