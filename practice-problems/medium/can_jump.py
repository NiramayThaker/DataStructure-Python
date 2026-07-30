class Solution:
    def canJump(self, nums) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True

        return True


# Approach

# Initialize a variable to keep track of the farthest index that can be reached while traversing the array.

# Iterate through each index and check whether the current index is reachable. If the current index is beyond the maximum reachable position, return false.

# Update the farthest reachable position by considering the maximum distance that can be achieved from the current index.

# If the farthest reachable position reaches or exceeds the last index, return true; otherwise, continue checking until all elements are processed.

# Time Complexity
# O(n), where n is the length of the array, because each element is visited once.

# Space Complexity
# O(1), because only a constant amount of extra memory is used.