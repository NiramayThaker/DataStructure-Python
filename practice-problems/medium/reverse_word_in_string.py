# # Approach
# # 1) Break the sentence into words
# * Use split() to remove extra spaces and get a list of words.

# # 2) Traverse the words in reverse order
# * Start from the last word and move to the first.

# # 3) Build the reversed sentence
# * Append each word to the result with appropriate spacing.

# # 4) Return the final string
# * The newly built string is the sentence with reversed word order.


# Approch - 1
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# Approch - 2
class Solution:
    def reverseWords(self, s: str) -> str:
        ll_s = s.split()
        final_s = ""
        
        for i in range(len(ll_s) - 1, -1, -1):
            final_s += (ll_s[i] + " ") if i != 0 else (ll_s[i])
        
        return final_s
