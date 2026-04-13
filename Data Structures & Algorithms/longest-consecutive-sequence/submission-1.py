class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : return 0

        nums.sort()
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1

        firstElement = nums[0]
        nextElement = firstElement + 1

        ans = 1
        m = 0

        for i in count:
            if i == firstElement:
                pass
            elif i == nextElement:   # ✅ FIX
                ans += 1
            else:
                m = max(m, ans)
                firstElement = i
                ans = 1             # ✅ FIX
        
            nextElement = i + 1     # ✅ better update

        m = max(m, ans)             # ✅ FIX
        return m