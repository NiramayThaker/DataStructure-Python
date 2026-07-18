class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_num:int = -1
        min_num:list[int] = nums[0]

        for i in range(1, len(nums)):
            max_num = max(max_num, nums[i] - min_num)
            min_num = min(nums[i], min_num)

        return max_num if max_num != 0 else -1
                
