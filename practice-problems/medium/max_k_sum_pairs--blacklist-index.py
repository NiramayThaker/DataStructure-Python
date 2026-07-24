class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        black_listed_idx = []
        cnt = 0

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if i in black_listed_idx:
                    break

                if j in black_listed_idx:
                    continue

                elif nums[i] + nums[j] == k:
                    cnt += 1
                    black_listed_idx.append(i)
                    black_listed_idx.append(j)

        return cnt



"""
Approach

Use nested loops to check every possible pair of elements and determine if their sum equals k.
Maintain a blacklist of used indices to prevent already paired elements from being reused.
Whenever a valid pair is found, increase the count and mark both indices as unavailable.
Continue checking remaining combinations, but this approach performs unnecessary comparisons and becomes inefficient for large inputs.

Complexity

Time Complexity: O(n³) — Nested loops take O(n²), and checking index existence in a list takes O(n) in the worst case.
Space Complexity: O(n) — The blacklist stores indices of paired elements.
"""