class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        # child for greed
        # cookie for size of cookie
        child = cookie = 0
        # g = [1,2,3], s = [1,1] or g = [2,2], s = [1,2,3]

        # if cookie size >= childs greed, we increase g by 1

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
            
        return child


