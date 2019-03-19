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
