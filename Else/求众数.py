class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=int(len(nums)/2)
        return sorted(nums)[n]
