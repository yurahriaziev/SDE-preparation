class Solution:
    def minimumOperations(self, nums):
        if sum(nums) == 0:
            return 0
        
        op_count = 0
        while sum(nums) != 0:
            x_min = min([i for i in nums if i != 0])
            # print('x_min', x_min)
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= x_min
            op_count += 1
            # print('nums', nums)
            # print('sum of nums', sum(nums))
        
        return op_count

sol = Solution()
print(sol.minimumOperations([0,0,1]))