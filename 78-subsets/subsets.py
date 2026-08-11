class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        def sub(index):
            if index==len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[index])
            sub(index+1)

            curr.pop()
            sub(index+1)
        sub(0)
        return(ans)