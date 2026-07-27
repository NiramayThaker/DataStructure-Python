# Code
class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for char in s:
            stk.pop() if char == '*' else stk.append(char)
        
        return "".join(stk)


# Approach

# 1. Use a stack to store characters that are not removed.
# 2. Traverse the string character by character:
#    - If the character is not '*', push it into the stack.
#    - If the character is '*', remove the most recent character from the stack using pop().
# 3. After processing all characters, join the remaining stack elements to form the final string.

# # Complexity
# - Time complexity: O(n)

# - Space complexity: O(n)
