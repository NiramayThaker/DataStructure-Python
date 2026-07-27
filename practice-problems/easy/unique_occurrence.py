class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        occ_list = {}

        for i in arr:
            occ_list[i] = occ_list.get(i, 0) + 1
        
        dup = occ_list.values()
        return len(dup) == len(set(dup))
        

        # dup_cnt = []
        # for i in occ_list:
        #     if occ_list[i] not in dup_cnt:
        #         dup_cnt.append(occ_list[i])
        #     else:
        #         return False
        
        # return True


# Approach:
# 1. Traverse the array and use a hash map to count the frequency of each element.
# 2. Iterate through the frequency map and check each occurrence count.
# 3. Store each unique occurrence count in a list; if a count already exists, return False.
# 4. If all occurrence counts are unique, return True.

# Time Complexity:
# O(n)
# - Counting frequencies takes O(n), and checking occurrence counts takes O(k), where k is the number of distinct elements. Overall, O(n).

# Space Complexity:
# O(n)
# - A hash map stores element frequencies, and an additional list stores unique occurrence counts.