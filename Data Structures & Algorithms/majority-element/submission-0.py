class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
            # 5 : 4, 1:3
        maxVal = 0
        for i in count.values():
            maxVal = max(maxVal, i)
            # 4
        ans = 0
        for i in count:
            if count.get(i, 0) == maxVal:
                ans = i
        return ans
            