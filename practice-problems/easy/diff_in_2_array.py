class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [[i for i in s1 if i not in s2], [i for i in s2 if i not in s1]]



# Time Complexity:
# O(n + m)
# - Creating the two sets takes O(n + m), and checking differences also takes O(n + m).

# Space Complexity:
# O(n + m)
# - Two sets are used to store the unique elements from both arrays.