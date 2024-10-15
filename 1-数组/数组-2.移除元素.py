# 数组-2.移除元素

'''
给一个数组，再给定一个目标值。
在数组中删除等于这个目标值的元素，然后返回新数组的大小。
注意：
  数组是应该连续的类型相近的元素的一个集合    # 连续很重要 ！！！
  对数组的删除其实并不是直接删除，而是覆盖！
  在经过删除步骤以后，这个新数组的内存并没有发生变化。 大小是 X-1 ， 容量是 X
  数组是基于栈实现的
'''
#=======================================================================================================================
'''
学习来源：
UP ：url = ‘https://space.bilibili.com/525438321’
视频：url = 'https://www.bilibili.com/video/BV12A4y1Z7LP'
笔记：url = 'https://programmercarl.com/'
题目：url = 'https://leetcode.cn/problems/remove-element/description/'
'''
#=======================================================================================================================
'''
解题思路：
双指针法：
    1. 定义两个指针，一个指针用于遍历数组，另一个指针用于指向新数组的下标
    2. 初始时，left = 0
    3. 遍历数组，如果当前元素不等于目标值，则将该元素赋值给新数组的下标，并将新数组的下标加1
    4. 遍历结束后，返回新数组的下标，即为新数组的大小
    5. 注意：nums 的元素可能不在 0 到 k-1 之间，所以在返回 k 之前，需要将 nums[0] 到 nums[k-1] 排序

快指针的作用是遍历数组，慢指针作用的接受快指针遍历出的不等于target的元素   两个操作都是在一个数组上实现的
    此时该算法时间复杂度为O（N）   空间换时间

若不采用该算法，而是使用双for循环，那么，此时时间复杂度为 O（N^2）
'''
#=======================================================================================================================
'''
例题来源：Leeetcode 27.  移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
用户评测：
评测机将使用以下代码测试您的解决方案：

int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''
#=======================================================================================================================
# 解题
#（版本一）快慢指针法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

'''
#（版本二）暴力法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:  # 找到等于目标值的节点
                for j in range(i + 1, l):  # 移除该元素，并将后面元素向前平移
                    nums[j - 1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l


# 相向双指针法
# 时间复杂度 O(n)
# 空间复杂度 O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left

'''

if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))