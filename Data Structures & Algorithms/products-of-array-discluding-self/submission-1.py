class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_val = 1
        for i in range(len(nums)):
            prefix.append(prefix_val)
            prefix_val *= nums[i]

        suffix = [1] * len(nums)
        suffix_val = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output