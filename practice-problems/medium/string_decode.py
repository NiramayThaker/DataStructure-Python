class Solution:
    def decodeString(self, s: str) -> str:
        valid_str = []
        s = list(s)

        for i in s:
            if i != ']':
                valid_str.append(i)
            else:
                cur_str = ""
                while valid_str[-1] != '[':
                    cur_str = valid_str.pop() + cur_str
                valid_str.pop()

                cur_num = ""
                while valid_str and valid_str[-1].isdigit():
                    cur_num = valid_str.pop() + cur_num
                
                cur_str = int(cur_num) * cur_str
                valid_str.append(cur_str)
        
        return "".join(valid_str)


# ## Approach

# Use a stack to process the encoded string one character at a time.

#  Traverse each character in the string.
#  If the character is not ], push it onto the stack.
#  When ] is encountered:

#    Pop characters until [ is found to obtain the encoded substring.
#    Remove the [ from the stack.
#    Pop all consecutive digits before [ to form the repetition count.
#    Repeat the decoded substring count times.
#    Push the expanded string back onto the stack.
#  After processing the entire string, join all elements remaining in the stack to obtain the final decoded string.

# This approach naturally handles nested encodings because inner expressions are decoded first and pushed back onto the stack before the outer expression is processed.

# ---

# ## Complexity

#  Time Complexity: O(n)

#    Each character is pushed onto and popped from the stack at most once.
#    Although string concatenation and repetition occur, every character in the input is processed a constant number of times. Hence, the overall complexity is O(n), where n is the length of the input string. (If the decoded output is much larger than the input, the running time is proportional to the size of the decoded output.)

#  Space Complexity: O(n)

#    The stack stores characters and intermediate decoded strings.
#    In the worst case, it can hold all input characters, requiring O(n) auxiliary space (excluding the output string).
