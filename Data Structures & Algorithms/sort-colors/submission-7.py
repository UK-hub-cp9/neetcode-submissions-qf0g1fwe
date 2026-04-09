class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = {}  # Initialize an empty dictionary

        for i in nums:
        # Use .get(i, 0) to return 0 if the key 'i' is missing, then add 1
            counts[i] = counts.get(i, 0) + 1
        # Output: {2: 2, 0: 2, 1: 2}
        ptr = 0
        for i in range(counts.get(0, 0)):
            nums[ptr] = 0
            ptr += 1

        for i in range(counts.get(1, 0)):
            nums[ptr] = 1
            ptr += 1

        for i in range(counts.get(2, 0)):
            nums[ptr] = 2
            ptr += 1

