class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int x = INT_MAX;
        int y = INT_MAX;

        for(int i: nums) 
        {
            if(i <= x) x = i;
            else if(i <= y) y = i;
            else return true;
        }
        
        return false;
    }
};


/*
# Approach

1. **Keep track of the smallest element (`x`) seen so far.**

2. **Keep track of the smallest second element (`y`) that is greater than `x`.**

3. **Update `x` or `y` whenever a better (smaller) candidate is found.**

4. **If a number is greater than both `x` and `y`, then `x < y < current`, so an increasing triplet exists.**

---

### **Time Complexity**

* **O(n)** — Traverse the array only once.

### **Space Complexity**

* **O(1)** — Uses only two extra variables (`x` and `y`).
*/
