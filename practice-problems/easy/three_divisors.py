class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        
        if n <= 2:
            return False
        
        for x in range(1, n + 1):
            if n % x == 0:
                count += 1
        
        return (count == 3)