class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        x=len(nums)
        for i in range(1,x-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if nums[0]>nums[-1]:
            return 0
        else:
            return x-1
