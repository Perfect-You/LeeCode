'''会超出时间限制，因为差不多有三层循环，哎，好烦'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=0
        j=0
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            while j<len(nums) and k>j:
                if nums[i]<nums[j]<nums[k]:
                    return True
                elif k>j+1:
                    k-=1
                elif k==j+1:
                    k=len(nums)-1
                    j+=1   
            i+=1
        return False
'''当当当当，新的答案来啦，别人的方法，很巧妙啊'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        x=2**32-1
        y=2**32-1
        for i in nums:
            if i<=x:
                x=i
            elif i<=y and i>x:
                y=i
            else:
                return True
        return False
