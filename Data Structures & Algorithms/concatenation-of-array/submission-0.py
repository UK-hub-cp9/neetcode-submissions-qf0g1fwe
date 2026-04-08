class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [ 0 for i in range(2*len(nums))]
        # ans = [ 0,0,0,0]
        for i in range(len(nums)): # for i in range(2)
            ans[i] = nums[i]       # 0 = 1
            # ans = [1,2,0,0]
        ptr = 0
        for i in range(len(nums), len(ans)):
            ans[i] = nums[ptr]
            ptr+=1
            
        return ans