#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

from typing import List


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            newNums = []
            for i in range(k):
                newNums.append(nums[i])

            self.buildMaxHeapify(newNums)

            # 求最大
            for i in range(k,len(nums)):
                if nums[i] > newNums[0]:
                    self.replace(nums[i],newNums)

            # 求最小 
            # for i in range(k,len(nums)):
            #     if nums[i] < newNums[0]:
            #         self.replace(nums[i],newNums)

            return newNums[0]

    # 建堆，本题是最小堆
    def buildMaxHeapify(self,nums):
        for i in range(len(nums)//2-1,-1,-1):
            self.siftDown(i,nums)

    #删除第一个并下滤
    def replace(self,value,newNums):
        newNums[0] = value
        self.siftDown(0,newNums)

    # 下滤
    def siftDown(self,index,nums):
        # 非叶子节点数量 floor(size/2)
        # 叶子节点数量 ceil(size/2)
        size = len(nums)
        half = size//2 
        element = nums[index]
        while index < half:
            childIndex = 2*index + 1

            if childIndex + 1 < size and self.compare(nums[childIndex+1],nums[childIndex])>0:
                childIndex = childIndex + 1

            childElement = nums[childIndex]
            if self.compare(element,childElement) >= 0:
                break

            nums[index] = childElement
            index = childIndex
        nums[index] = element


        # 上滤 
    def siftUP(self,index,nums):
        size = len(nums)
        element = nums[index]
        while index > 0:
            parentIndex = (size-1)//index
            parentElement = nums[parentIndex]
            if self.compare(parentElement,element) >= 0:
                break

            nums[index] = parentElement
            index = parentIndex

        nums[index] = element

    def compare(self,value1,value2):
        # 最小堆 本题用最小堆
        return value2 - value1
        # 最大堆
        return value1 - value2

# @lc code=end


sol = Solution()
print(sol.findKthLargest([3,2322,10,1,8,132,59,6],4))
 