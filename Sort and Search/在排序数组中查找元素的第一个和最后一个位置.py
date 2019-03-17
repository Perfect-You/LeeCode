class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        re=[]
        for i in range(len(nums)):
            if nums[i]==target:
                re.append(i)
        if len(re)==0:
            return [-1,-1]
        else:
            return [re[0],re[-1]]
