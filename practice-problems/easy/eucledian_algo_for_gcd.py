class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)

        # Formula:
        # gcd(a, b) = (b, a%b)
        
        a, b = min_num, max_num
        while b > 0:
            a, b = b, (a%b)

        return a


# Test Cases
# nums = [3,3]
# nums = [7,5,6,8,3]
# nums = [2,5,6,9,10]