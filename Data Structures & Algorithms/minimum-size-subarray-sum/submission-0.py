import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        summ = 0
        res = sys.maxsize

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                res = min(res, r - l + 1)
                summ -= nums[l]
                l += 1
        
        if res == sys.maxsize:
            return 0
        else:
            return res