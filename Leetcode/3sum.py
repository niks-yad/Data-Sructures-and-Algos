class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        hasher = {}
        counter = 0
        prevNum = None
        for i in range(len(nums)):
            
            firstNum = nums[i]
            if firstNum != prevNum:
                numbers = nums[i+1:len(nums)]
                target = 0 - firstNum
                l = 0
                r = len(numbers)-1
                while l<r:
                    if numbers[l] + numbers[r] > target:
                        r -= 1

                    elif numbers[l] + numbers[r] < target:
                        l += 1

                    elif numbers[l] + numbers[r] == target:
                        val = [firstNum,numbers[l],numbers[r]]
                        val.sort()
                        valTup = (val[0], val[1], val[2])
                        if valTup not in hasher:
                            hasher[valTup] = 1
                            ans.append(val)
                        l += 1
                        r -= 1
            prevNum = firstNum

            

        return ans