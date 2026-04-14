class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            # act
            count = [0] * 26
            # [ 0,0,,.....0] 26 0's
            for c in s:
                
                count[ord(c) - ord("a")]+=1
            
            res[tuple(count)].append(s)
            #[ (1,0,1,...0) : act ]
        return list(res.values())