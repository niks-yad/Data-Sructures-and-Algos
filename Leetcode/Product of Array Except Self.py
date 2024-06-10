class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) # not extra memory
        ans[0] = nums[0]
        # prefix = left to right
        for i in range(1,len(nums)):
            ans[i] = nums[i] * ans[i-1]

        # postfix = right to left
        postfix = 1
        for i in range(len(nums)-1,0,-1):
            ans[i] = ans[i-1] * postfix
            postfix = postfix * nums[i]

        ans[0] = postfix

        return ans

        