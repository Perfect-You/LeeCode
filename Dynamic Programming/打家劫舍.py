class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        else:
            nums[1]=max(nums[0],nums[1])
            for i in range(1,len(nums)-1):
                nums[i+1]=max(nums[i],nums[i-1]+nums[i+1])
            return nums[-1]
