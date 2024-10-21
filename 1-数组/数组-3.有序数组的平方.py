# 数组-3.有序数组的平方

'''
给定一个有序数组，需要返回一个说有元素平方之后，依然是有序的一个数组
                注：（数组中有负数）
'''
#=======================================================================================================================
'''
# 学习来源
UP ：url = ‘https://space.bilibili.com/525438321’
视频：url = 'https://www.bilibili.com/video/BV1QB4y1D7ep'
笔记：url = 'https://programmercarl.com/'
题目：url = 'https://leetcode.cn/problems/squares-of-a-sorted-array/description/'
'''
#=======================================================================================================================
'''
# 图文
    I------------------I-------------------I-------------------I-------------------I
i(left)---->                              MID                              <----j(right)
                     
'''
#=======================================================================================================================
'''
# 解题思路 ---------> 用时间换空间
双指针解法思路：
    1.给定一个数组，数组中因为有负数，所以平方之后的最大值一定在两遍，不可能会在中间
    2.因此我们可以用两个指针，逐步向中间靠拢的一个操作，得到一个由大到小的数组
    3.在更新新的数组时，下标由大到小来进行更新即可
    4.无序数组可以先平方再排序

解题流程：
    result  # 定义一个数组
    k = nums - 1 # 定义一个索引下标   # 最大索引是数量-1
    i = 0 , j = nums - 1  # 定义两个下标
    for(i <= j) :   # 当i = j 时，取到数据中间值 ， 如果不取 “=” ， 则会少一个元素    # while(i <= j)
        if nums[i] * nums[i] > nums[j] * nums[j] :
            result[k] = nums[i] * nums[i]
            k = k - 1
            i = i + 1
        
        else :
            result[k] = nums[j] * nums[j]
            k = k - 1
            j = j - 1
        
    return result        
    
    # 左右两侧的指针网中间缩，与此同时，进行比较
    如果 left 比 right 大，那么将左侧的值赋值给result
                同时，left前进一步 往中间扩张 进行操作 left++
    如果 right 比 left 大，那么将右侧的值赋值给result
                同时，right后退一步，往中间缩 进行操作 right--
    
'''
#=======================================================================================================================
'''
# 例题来源：Leeetcode 977.  有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
 

进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题
'''
#=======================================================================================================================
# 求解
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        k = len(nums) - 1

        left = 0
        right = len(nums) - 1

        while (left <= right):
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result.append(nums[left] * nums[left])
                k = k - 1
                left = left + 1

            else:
                result.append(nums[right] * nums[right])
                k = k - 1
                right = right - 1

        return result[::-1]


# 程序入口
if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    result = Solution().sortedSquares(nums)
    print(result)