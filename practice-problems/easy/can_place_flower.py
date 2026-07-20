# Approach

# <!-- Describe your approach to solving the problem. -->
# 1) Traverse every plot exactly once.

# 2) For each plot, check if the current plot and both neighbors (when they exist) are empty.

# 3) If planting is possible, plant immediately (greedy choice).

# 4) Stop early once you've planted n flowers.

# Complexity

# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(n)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(1)


# Code
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return n <= 0
