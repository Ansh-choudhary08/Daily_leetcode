from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = defaultdict(int)

        for ch in t:
            need[ch] += 1

        window = defaultdict(int)

        l = 0
        have = 0
        need_count = len(need)

        start = 0
        min_len = float('inf')

        for r in range(len(s)):

            window[s[r]] += 1

            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            while have == need_count:

                # Current window is valid
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                # Remove left character
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]