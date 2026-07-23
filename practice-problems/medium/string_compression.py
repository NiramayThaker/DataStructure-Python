# Code
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = str(chars[0])
        cnt = 1

        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                cnt +=1
            else:
                if cnt != 1:
                    s += str(cnt)
                s += chars[i]
                cnt = 1
        
        if cnt != 1:
            s += str(cnt)

        chars[:] = list(s)
        return len(chars) 


# # Approach
# #### Step-by-Step

# ```python
# s = str(chars[0])
# cnt = 1
# ```

# * `s` stores the compressed result.
# * Start with the first character.
# * `cnt` keeps track of the frequency of the current character.

# ---

# ```python
# for i in range(1, len(chars)):
# ```

# * Iterate from the second character onwards.

# ---

# ```python
# if chars[i] == chars[i-1]:
#     cnt += 1
# ```

# * If the current character is the same as the previous one, increase the count.

# ---

# ```python
# else:
#     if cnt != 1:
#         s += str(cnt)
#     s += chars[i]
#     cnt = 1
# ```

# * A different character means the previous group has ended.
# * If its count is greater than 1, append the count.
# * Append the new character.
# * Reset the count to 1.

# ---

# ```python
# if cnt != 1:
#     s += str(cnt)
# ```

# * After the loop, process the last group since it hasn't been added yet.

# ---

# ```python
# chars[:] = list(s)
# ```

# * Replace the original array contents with the compressed characters **in-place**.

# ---

# ```python
# return len(chars)
# ```

# * Return the new length of the compressed array.

# ---


# * Traverse the array once while counting consecutive occurrences of the current character.
# * Whenever the character changes, append the previous character and its count (only if count > 1) to the result.
# * Reset the counter for the new character and continue processing the remaining array.
# * After the traversal, process the final group and update the original array in-place with the compressed result.

# ### Time Complexity

# **O(n)** – Each character is visited exactly once.

# ### Space Complexity

# **O(n)** – Uses an additional string to build the compressed result before copying it back.


# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

