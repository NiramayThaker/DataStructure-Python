class Solution:
    def jump(self, nums) -> int:
        n = len(nums)

        if n == 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jumps



# Approach (4 Steps):

# If the array has only one element, no jumps are needed, so return 0.

# Traverse the array while tracking the farthest index that can be reached from all positions within the current jump range.

# When the current index reaches the end of the current jump range, increment the jump count and update the current range to the farthest reachable index.

# Continue expanding the reachable range until it reaches or passes the last index, then return the total number of jumps.

# Time Complexity: O(n)
# Space Complexity: O(1)