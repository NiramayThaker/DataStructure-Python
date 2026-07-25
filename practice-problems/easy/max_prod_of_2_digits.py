# Code 1
class Solution:
    def maxProduct(self, n: int) -> int:
        v1, v2 = sorted(str(n))[-2:]
        return int(v1) * int(v2)


# 1. Extract all digits of the number and store them in a list.
# 2. Find every possible pair of digits.
# 3. Calculate the product of each pair.
# 4. Return the maximum product obtained.


# Code 2
class Solution:
    def maxProduct(self, n: int) -> int:
        mx_1 = 0
        mx_2 = 0

        while n > 0:
            cur = n % 10

            if cur >= mx_1:
                mx_2 = mx_1
                mx_1 = cur
            elif cur > mx_2:
                mx_2 = cur
            
            n //= 10
        
        return mx_1 * mx_2

# 1. Initialize two variables, `max1` and `max2`, to store the largest and second-largest digits.
# 2. Traverse the number digit by digit using `% 10` and `// 10`.
# 3. Update `max1` and `max2` whenever a larger or second-largest digit is found.
# 4. Return the product `max1 * max2`.