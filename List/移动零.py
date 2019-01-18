class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x=0
        i=0
        while i+x<len(nums):
            if nums[i]==0:
                x+=1
                del nums[i]
                nums.append(0)
            else:
                i+=1
