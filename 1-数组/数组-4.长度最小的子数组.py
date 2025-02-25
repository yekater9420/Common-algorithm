# 数组-4.长度最小的子数组
'''
长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的
子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

大于等于s的，连续的，最小长度的区间
'''
#=======================================================================================================================
'''
# 学习来源
UP ：url = ‘https://space.bilibili.com/525438321’
视频：url = 'https://www.bilibili.com/video/BV1tZ4y1q7XE'
笔记：url = 'https://programmercarl.com/'
题目：url = 'https://leetcode.cn/problems/minimum-size-subarray-sum//'
'''
#=======================================================================================================================
# 解题思路
'''
# 滑动窗口法：  -----》双指针
for(j )
# 在滑动窗口法中：j表示终止位置，但是重点难点在于：如何移动起始位置呢？？？？

for（j=0,j<=numsize,j++）
sum+=nums[j]
滑动窗口法：
while(sum>=s)
sum-=nums[i]
i++
if(j-i+1<minlen)
minlen=j-i+1
'''
'''
实现了一个在数组中寻找子数组的最小长度的算法，该子数组的和大于或等于给定的目标值 `s`。具体来说，它使用的是滑动窗口技术，这是一种常见的用于解决子数组或子字符串问题的算法。

### 实现原理

1. **初始化变量**：
   - `l`：数组的长度。
   - `left`：滑动窗口的左边界，初始值为0。
   - `right`：滑动窗口的右边界，初始值为0。
   - `min_len`：记录满足条件的子数组的最小长度，初始值为正无穷大。
   - `cur_sum`：当前滑动窗口内元素的和，初始值为0。

2. **滑动窗口**：
   - 使用一个 `while` 循环，右边界 `right` 从0开始向右移动，每次移动时将 `nums[right]` 加到 `cur_sum` 中。
   - 当 `cur_sum` 大于或等于目标值 `s` 时，进入内层 `while` 循环：
     - 更新 `min_len` 为当前窗口长度 `right - left + 1` 和 `min_len` 中的较小值。
     - 将 `nums[left]` 从 `cur_sum` 中减去，并将左边界 `left` 向右移动一位。
   - 右边界 `right` 继续向右移动。

3. **返回结果**：
   - 如果 `min_len` 仍为正无穷大，说明没有找到满足条件的子数组，返回0。
   - 否则，返回 `min_len`。

### 用途

这段代码可以用于解决以下问题：
- 给定一个数组和一个目标值，找到和大于或等于目标值的最小子数组的长度。

### 注意事项

- 输入数组 `nums` 和目标值 `s` 必须是整数。
- 如果数组中所有元素的和都小于目标值 `s`，则返回0。
- 该算法的时间复杂度为 O(n)，其中 n 是数组的长度，因为每个元素最多被访问两次（一次被加入窗口，一次被移出窗口）。
'''
#=======================================================================================================================
'''
# 例题来源：Leeetcode 209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 
子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

提示：
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 
进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
'''
#=======================================================================================================================
# 解题
#暴力法：
class Solution_violence:
    def minSubArrayLen_violence(self, s: int, nums: list[int]) -> int:
        l = len(nums)
        min_len = float('inf')

        for i in range(l):
            cur_sum = 0
            for j in range(i, l):
                cur_sum += nums[j]
                if cur_sum >= s:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len if min_len != float('inf') else 0


# 滑动窗口法：
class Solution_move_windows:
    def minSubArrayLen_move_windows(self, s: int, nums: list[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0  # 当前的累加值

        while right < l:
            cur_sum += nums[right]

            while cur_sum >= s:  # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0

if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(f"暴力法：",Solution_violence().minSubArrayLen_violence(s, nums))
    print(f"滑动窗口法：",Solution_move_windows().minSubArrayLen_move_windows(s, nums))