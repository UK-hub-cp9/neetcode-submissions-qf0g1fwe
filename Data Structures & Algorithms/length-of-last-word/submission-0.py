class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = s.split()
        l = len(words)
        # Output: ['hello', 'world']
        lastword = words[l-1]
        return len(lastword)
