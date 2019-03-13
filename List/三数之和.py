class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        new=[]
        nums.sort()
        x=len(nums)
        for i in range(x-2):
            if i==0 or nums[i]>nums[i-1]:
                j=i+1
                k=x-1
                while j<k:
                    if nums[i]+nums[j]+nums[k]==0:
                        new=[nums[i],nums[j],nums[k]]
                        l.append(new)
                        j+=1
                        k-=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                        while j<k and nums[k]==nums[k+1]:
                            k-=1
                    if nums[i]+nums[j]+nums[k]>0:
                        k-=1
                    if nums[i]+nums[j]+nums[k]<0:
                        j+=1
        return l
