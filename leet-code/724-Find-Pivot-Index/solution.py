class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        l_sum, r_sum = 0, sum(nums)
        for i, n in enumerate(nums):
            r_sum -= n
            if l_sum == r_sum:
                return i
            l_sum += n
        return -1
        
        ### alternate using while loop, slightly different logic
        # p = 0
        # l_sum = 0
        # r_sum = sum(nums) - nums[p]
        # while True:
        #     if l_sum == r_sum:
        #         return p
        #     l_sum += nums[p]
        #     p += 1
        #     if p >= len(nums): break
        #     r_sum -= nums[p]
        # return -1