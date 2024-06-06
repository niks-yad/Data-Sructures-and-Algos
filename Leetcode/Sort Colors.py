class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        i = 0
        l = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
            elif nums[i] == 2:
                swap(r,i)
                r -= 1
                i -= 1
            i += 1

        return nums