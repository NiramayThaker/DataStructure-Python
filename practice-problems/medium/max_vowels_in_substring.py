# Approach - 1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        count = 0
        answer = 0

        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            if right - left + 1 == k:
                answer = max(answer, count)

                if s[left] in vowels:
                    count -= 1

                left += 1

        return answer

# 1. Initialize two pointers (`left`, `right`) and a counter to track vowels in the current window.
# 2. Expand the window by moving `right`; if the current character is a vowel, increment the count.
# 3. When the window size becomes `k`, update the maximum vowel count.
# 4. Before sliding the window, remove the leftmost character (decrement the count if it's a vowel), then move `left` forward.


# Approach - 2
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = answer = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        answer = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            answer = max(answer, count)

        return answer


# 1. Count the number of vowels in the first window of size `k`.
# 2. Store this count as the initial maximum.
# 3. Slide the window one character at a time by adding the incoming character and removing the outgoing character.
# 4. Update the maximum vowel count after processing each new window.
