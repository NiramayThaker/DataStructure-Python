class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for a in asteroids:
            while stk and a < 0 < stk[-1]:
                if -a > stk[-1]:
                    stk.pop()
                    continue
                elif -a == stk[-1]:
                    stk.pop()
                break
            else:
                stk.append(a)
        
        return stk


# Approach
# - Initialize an empty stack to store surviving asteroids.
# - Iterate through each asteroid:
#   - If the current asteroid is moving left and the stack top is moving right, a collision occurs.
#   - Compare their sizes:
#     - If the current asteroid is larger, remove the top asteroid and continue checking for more collisions.
#     - If both asteroids are the same size, remove the top asteroid and destroy the current asteroid.
#     - If the stack asteroid is larger, destroy the current asteroid.
#   - If no collision occurs, add the current asteroid to the stack.
# - Return the stack containing the remaining asteroids.

# # Complexity
# - Time complexity:
# O(n)
# Each asteroid is pushed onto the stack once and removed at most once.

# - Space complexity:
# O(n)
# In the worst case, all asteroids survive and are stored in the stack.
