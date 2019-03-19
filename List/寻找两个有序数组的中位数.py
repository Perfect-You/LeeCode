class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        m=len(nums1)
        if m%2==0:
            re=(nums1[m//2]+nums1[m//2-1])/2
        if m%2!=0:
            re=nums1[m//2]
        return re
