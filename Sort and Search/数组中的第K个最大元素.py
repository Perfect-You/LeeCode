class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        x=len(nums)
        return nums[x-k]
