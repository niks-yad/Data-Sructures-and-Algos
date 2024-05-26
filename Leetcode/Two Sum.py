class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in hasher:
                return hasher[temp],i
            else:
                hasher[nums[i]] = i
