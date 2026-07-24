class Solution:
    def maxOperations(self, nums, k) -> int:

        freq = {}
        cnt = 0

        for num in nums:

            need = k - num

            if need in freq and freq[need] > 0:
                cnt += 1
                freq[need] -= 1

            else:
                freq[num] = freq.get(num, 0) + 1

        return cnt

### Approach

# 1. **Calculate the required complement** (`need = k - num`) for each number to find the value needed to create a valid pair.
# 2. **Use a hash map to store frequencies of unused numbers** so that complement lookup can be performed in constant time.
# 3. **If the required complement exists, form a pair immediately**, increment the count, and decrease its frequency to avoid reuse.
# 4. **If the complement is unavailable, store the current number's frequency** so future elements can pair with it.

# ### Complexity

# * **Time Complexity:** O(n) — Each element is processed once, with O(1) average hash map operations.
# * **Space Complexity:** O(n) — The hash map may store all elements in the worst case.
