
class Solution:     
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        a,b,c = 0,1,0
        for i in range(l-1):
            if nums[a] == nums[b]:
                b+=1
                c+=1
            else:
                a+=1
                nums[a] = nums[b]
                b+=1
        return len(nums) - c
            