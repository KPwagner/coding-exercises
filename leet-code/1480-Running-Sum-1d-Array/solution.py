class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for n in nums:
            if output == []:
                output.append(n)
            else:
                output.append(n + output[-1])
        return output
    
        ### alternate using output list as array, no appending
        # sums = [0 for n in nums]
        # for idx, n in enumerate(nums):
        #     if idx == 0:
        #         sums[idx] = n
        #     else:
        #         sums[idx] = n + sums[idx - 1]

        # return sums