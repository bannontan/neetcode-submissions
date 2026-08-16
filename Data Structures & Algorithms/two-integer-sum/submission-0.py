class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_hash:
                return [num_hash[complement], i]
            num_hash[nums[i]] = i