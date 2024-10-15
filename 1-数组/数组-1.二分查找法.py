# 数组-1.二分查找法

'''
二分查找法
1.什么是二分查找法：
    二分查找法是一种在有序数组中查找特定元素的算法。
    它通过将查找范围分成两半，然后根据目标元素与中间元素的比较结果，
    决定在左半部分还是右半部分继续查找，从而逐步缩小查找范围，直到找到目标元素或确定目标元素不存在。
    找到返回下标，找不到返回-1

2.二分查找法的时间复杂度：
    二分查找法的时间复杂度为 O(log n)，其中 n 是数组的长度。

3.二分查找法的适用条件：
    二分查找法适用于有序数组，即数组中的元素已经按照某种顺序排列。
    如果数组中的元素无序，二分查找法将无法正确工作。

4.二分查找法写代码时的注意事项
    在编写二分查找法的代码时，需要注意以下几点：
    1. 确保数组是有序的，否则二分查找法将无法正确工作。
    2. 在循环中，需要更新查找范围的左右边界，以逐步缩小查找范围。
    3. 在循环结束后，需要检查是否找到了目标元素，如果没有找到，则返回 -1。
    4. 在循环中，需要使用 while 循环，而不是 for 循环，因为 while 循环可以灵活地更新查找范围的左右边界。
    5. 在循环中，需要使用 mid = left + (right - left) // 2 来计算中间元素的索引，而不是 mid = (left + right) // 2，以避免整数溢出。
    6. 在循环中，需要使用 left = mid + 1 或 right = mid - 1 来更新查找范围的左右边界，而不是 left = mid 或 right = mid，以避免陷入死循环。
    7. 在循环中，需要使用 if nums[mid] == target 来判断是否找到了目标元素，而不是 if nums[mid] < target 或 if nums[mid] > target，因为二分查找法是查找等于目标元素的索引，而不是小于或大于目标元素的索引。
    # 最大的问题是边界的确定
    8.在写while循环的时候，这个 while（left < right）  ?   还是？
                            while（left <= right） ?
    9.在循环 if nums[mid] > target: 时更新右区间，此时，这个 right = mid-1 ? 还是 mid ? 还是 mid-1 ?

'''
#=======================================================================================================================
'''
概念：
  在区间搜索的时候，我们需要对这个区间的定义需要明确：
  1.搜索区间是左闭右闭[left,right]  还是左闭右开 [left , right)  还是右闭左开 （left , right]  这个会影响到对对边界条件的处理
      #Python里默认是左闭右开，所以定义 right = len(nums) - 1
  2.while循环是 left < right 还是 left <= right
  3.当 nums[mid] > target 时，right = mid - 1 还是 right = mid
  4.当 nums[mid] < target 时，left = mid + 1 还是 left = mid
'''
#=======================================================================================================================
'''
图像：
   I____________I____________I____________I
 left          mid          target       right
'''
#=======================================================================================================================
'''
### 左闭右闭写法：
原理：
  left = 0      target
  right = len(nums) - 1  #就是看这个target有没有在这个numsize的数组里
  while（left  <=  right） {   #开始进入循环   
                        ## 注：对于 <= 的情况是在区间 [left , right] ； 当left == right的时候，区间[left,right]依然有效
      mid= (left + right) // 2    # 对于numszie取中间值mid       ###  补充：/ 是浮点数除法（正常除法）  //是整数除法   %是取余
                                 # 注意：两个int型相加，有时候会越界，虽然这种题不会出现，但是不代表没有哟~
                                        所以，为了避免越界，我们也可以用 mid = left + (right - left) // 2   
      if nums[mid] > target ：   # 如果target小于中间值，那么target在mid的左边，所以，right = mid - 1
         right= mid - 1          # 在左闭右闭的区间里，我们已经判断这个middle所在的值已经大于target，
                                      所以这个nums[mid]已经不需要了，所以，right = mid - 1
      elif :
         nums[mid] < target :  # 如果target大于中间值，那么target在mid的右边，所以，left = mid + 1
         left = mid + 1          # 在左闭右闭的区间里，我们已经判断这个middle所在的值已经小于target，
      else :   
            return mid            # 如果target等于中间值，那么就找到了，直接返回mid
    return -1                     # 如果循环结束，都没有找到，那么就返回-1
  
************************************************************************************************************************
### 左闭右开写法：
原理：
  left = 0      target
  right = len(nums)   #就是看这个target有没有在这个numsize的数组里
  while（left  <  right） {   #开始进入循环
                        ## 注：对于 < 的情况是在区间 [left , right) ； 当left == right的时候，区间[left,right)已经无效
      mid= (left + right) // 2    # 对于numszie取中间值mid       ###  补充：/ 是浮点数除法（正常除法）  //是整数除法   %是取余  
      if nums[mid] > target ：   # 如果target小于中间值，那么target在mid的左边，所以，right = mid - 1
         right= mid              # 在左闭右开的区间里，我们已经判断这个middle所在的值已经大于target，
                                      所以这个nums[mid]已经不需要了，所以，right = mid
      elif :
       nums[mid] < target :  # 如果target大于中间值，那么target在mid的右边，所以，left = mid + 1
        left = mid + 1          # 在左闭右开的区间里，我们已经判断这个middle所在的值已经小于target，
      else :
            return mid            # 如果target等于中间值，那么就找到了，直接返回mid
    return -1                    # 如果循环结束，都没有找到，那么就返回-1

'''
#=======================================================================================================================
'''
学习来源：
视频：url = 'https://www.bilibili.com/video/BV1fA4y1o715/'
笔记：url = 'https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF'
题目：url = 'https://leetcode.cn/problems/binary-search/description/?envType=problem-list-v2&envId=binary-search'
'''
#=======================================================================================================================
'''
例题来源：Leeetcode 704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''
#=======================================================================================================================
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target :
                left = mid + 1

            else :
                return mid

        return -1

#text :
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums,target))

#text -----> 4