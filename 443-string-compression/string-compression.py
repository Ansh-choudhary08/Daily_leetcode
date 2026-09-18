class Solution:
    def compress(self, chars: list[str]) -> int:
        count=1
        prev=chars[0]
        s=chars[0]
        for i in range(1,len(chars)):
            if chars[i]==prev:
                count+=1
            else:
                if count>1:
                    s+=str(count)
                s+=chars[i]
                count=1
                prev=chars[i]
        if count>1:
            s+=str(count)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)