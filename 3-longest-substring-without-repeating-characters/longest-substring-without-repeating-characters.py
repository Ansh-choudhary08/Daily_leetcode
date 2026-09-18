class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        l=0
        ans=0
        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            ans=max(ans,len(ch))
        return ans