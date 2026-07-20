# # Approach - 1
# 1) Find the zero in list and then shift the next element at the place of zero 

# 2) Keep the count of the zero while shifting everytime

# 3) At last add all the zero's at the end of the same list

# # Approach - 2
# 1) Create 2 pointer 1st to keep track of zero and 2nd to find non-zero value

# 2) If you see zero in list pause the main loop and start another loop which finds non-zero value from that index

# 3) Once non-zero value is found swap it with zero and increment the pointers to find rest of the value 


# Code
# Approch - 1 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1


# Approch - 2 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_ptr = 0
        swap_ptr = zero_ptr + 1
        l_nums = len(nums)

        while zero_ptr < l_nums:
            if nums[zero_ptr] == 0:
                while swap_ptr < len(nums):
                    if nums[swap_ptr] != 0:
                        nums[zero_ptr], nums[swap_ptr] = nums[swap_ptr], nums[zero_ptr]
                        break
            
                    swap_ptr += 1
                
            zero_ptr += 1
            swap_ptr = zero_ptr + 1
