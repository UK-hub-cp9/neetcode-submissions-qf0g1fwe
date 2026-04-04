class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ptr = 1
        for i in range(len(nums) - 1):
            if ptr < len(nums):
                if nums[ptr] == nums[i]:
                    return True
                else:
                    ptr += 1
        return False