class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = 1

        for char in s:
            rows[curr_row] += char

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)


# Approach:

# Handle the edge case by returning the original string if there is only one row or the number of 
# rows is greater than or equal to the string length, since no zigzag pattern can be formed.

# Create a list for each row and simulate writing characters into the zigzag pattern by maintaining 
# the current row index and the direction of movement (down or up).

# Traverse each character in the string, append it to the current row, and reverse 
# the direction whenever the top or bottom row is reached.

# Concatenate all rows after processing every character to obtain the final zigzag converted string.

# Time Complexity
# O(n), where n is the length of the string, because each character is visited and placed into a row exactly once.

# Space Complexity
# O(n), as all characters are stored in the row lists before being combined into the final string.