# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        nums = []
        depths = []
        maxdepth = [0]
        
        def depthHelper(nestList, depth):
            maxdepth[0] = max(maxdepth[0], depth)
            for nestItem in nestList:
                if nestItem.isInteger():
                    nums.append(nestItem.getInteger())
                    depths.append(depth)
                else:
                    depthHelper(nestItem.getList(), depth + 1)
                
        depthHelper(nestedList, 1)
        result = 0
        for i in range(len(nums)):
            result += nums[i] * (maxdepth[0] - depths[i] + 1)
        return result

# MATH!
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        sumNums = [0]
        sumProd = [0]
        maxdepth = [0]
        
        def depthHelper(nestList, depth):
            maxdepth[0] = max(maxdepth[0], depth)
            for nestItem in nestList:
                if nestItem.isInteger():
                    item = nestItem.getInteger()
                    sumNums[0] += item
                    sumProd[0] += item * depth
                else:
                    depthHelper(nestItem.getList(), depth + 1)
                
        depthHelper(nestedList, 1)
        return (maxdepth[0] + 1) * sumNums[0] - sumProd[0]