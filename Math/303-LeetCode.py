#https://leetcode.com/problems/range-sum-query-immutable/discuss/75192/Java-simple-O(n)-init-and-O(1)-query-solution


# It's brute force solution

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)