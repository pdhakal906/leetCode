class Solution(object):
    def twoSum(self, nums, target):
        indexes = []
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    indexes.append(i)
                    indexes.append(j)
        return indexes

sol = Solution()
print(sol.twoSum([3,3], 6))
print(sol.twoSum([3,2,4], 6))

