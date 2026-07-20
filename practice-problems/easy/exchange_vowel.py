# # Approach
# 1) Identify what actually needs to change.
# Only the vowels are reversed—consonants remain in their original positions.

# 2) Use two pointers from opposite ends.
# Start one pointer from the left and one from the right to efficiently locate the next pair of vowels to swap.

# 3) Skip irrelevant characters.
# Move each pointer until it finds a vowel, avoiding unnecessary operations on consonants.

# 4) Swap and continue inward.
# Once both pointers are on vowels, swap them, then move both pointers toward the center until they meet.

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(n)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(n)


# Code
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="aeiouAEIOU"
        
        s = list(s)
        l_ptr = 0
        r_ptr = len(s)-1

        while l_ptr < r_ptr:
            while l_ptr < r_ptr and s[l_ptr] not in vowel:
                l_ptr += 1
            while l_ptr < r_ptr and s[r_ptr] not in vowel:
                r_ptr -= 1
            
            s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]
            l_ptr += 1
            r_ptr -= 1
        
        return "".join(s)
