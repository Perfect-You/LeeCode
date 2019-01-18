class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for index,num in enumerate(nums):
            another_num=target-num
            if another_num in dict:
                return [dict[another_num],index]
            dict[num]=index
