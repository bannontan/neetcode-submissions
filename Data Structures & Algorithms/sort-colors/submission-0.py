class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = 1
        while i < len(nums):
            if i == 0:
                i += 1
            if nums[i] >= nums[i-1]:
                i += 1
            else:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                i -= 1