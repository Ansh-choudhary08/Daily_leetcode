class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found=0
        tp=0
        sp=0
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        while tp<len(t):
            if t[tp]==s[sp]:
                sp+=1
                found+=1
            if found==len(s):
                return True
            tp+=1
        return False

