from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        currSum = 0
        count = 0

        for num in nums:
            currSum += num

            count += mp[currSum - k]

            mp[currSum] += 1

        return count