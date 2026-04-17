class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxVol = 0
        n = len(height)

        i = 0
        j = n - 1

        while i < j:
            currVol = (j - i) * min(height[i], height[j])
            maxVol = max(maxVol, currVol)

            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxVol
