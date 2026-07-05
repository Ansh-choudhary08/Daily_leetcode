class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=len(nums)
        a=[]
        if 0 in nums:
            for i in range(b):
                if nums[i]==0:
                    a.append(0)
        if 1 in nums:
            for i in range(b):
                if nums[i]==1:
                    a.append(1)
        if 2 in nums:
            for i in range(b):
                if nums[i]==2:
                    a.append(2)
        for i in range(b):
            nums[i]=a[i]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna