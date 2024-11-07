# 数组-5.螺旋矩阵II
'''
螺旋矩阵II：
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
'''
#=======================================================================================================================
'''
# 学习来源
UP ：url = ‘https://space.bilibili.com/525438321’
视频：url = 'https://www.bilibili.com/video/BV1SL4y1N7mV?'
笔记：url = 'https://programmercarl.com/'
题目：url = 'https://leetcode.cn/problems/spiral-matrix-ii/description/'
'''
#=======================================================================================================================
# 解题思路
'''
关键在于边界处理，这个矩阵边界上的四个点
四个角应该当做下一个边的起点
'''
#￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
# 错误思路
'''
每条边的处理规则不一样
'''
#￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
# 正确思路
# 循环不变量
'''
左闭右开
取变量循环时，应该保证每一次分数组都要保存一定的数量
每次处理边时，只处理第一个节点，最后一个不处理
输入边长n，则--------> 圈数为 n//2 # 为什么除以2呢，因为把矩阵上下切开，上半边有几条边就几圈  # 转一圈两行两列
                    # 进行判断：如果输入的边长n为奇数，则最中间的元素需要单独处理    
                              如果输入的边长n为偶数，则最中间的元素不需要单独处理
定义起始 startx, starty = 0, 0  这个起始位置每一圈其实都是会变的
定义圈数 loop = n // 2
i ， j 分别是行和列，每次循环到边界后更新i，j          [i , j]

向右遍历，行还是第i行，列由0自增到len(num)-1  |  数组[i , j]中的i表示行，j表示列，所以在数学上沿着x轴递增的话也就是在数组中j在递增
向下遍历，列还是第j列，行由0自增到len(num)-1  |  数组[i , j]中的i表示行，j表示列，所以在数学上沿着y轴递增的话也就是在数组中i在递增
向左遍历，行还是第i行，列由len(num)-1递减到0  |  数组[i , j]中的i表示行，j表示列，所以在数学上沿着x轴递减的话也就是在数组中j在递减
向上遍历，列还是第j列，行由len(num)-1递减到0  |  数组[i , j]中的i表示行，j表示列，所以在数学上沿着y轴递减的话也就是在数组中i在递减

那如何表示终止位置呢？：
终止位置：终止位置随每一圈不断改变。需要用一个终止变量----> offset来表示，初始值为1，每次循环到边界后更新offset
当 offset >= len(num) - 1 就表示到达了边界，此时不再需要对该方向进行循环

'''
#=======================================================================================================================
'''
例题来源：Leeetcode 59. 螺旋矩阵II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
1 ----> 2 ----> 3
                |
                |                
8 ----> 9 ----> 4
|               |   
|               |
7 <---- 6 <---- 5  

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]

提示：
1 <= n <= 20
'''
#=======================================================================================================================
# 解题
class Solution_1:
    def generateMatrix_1(self, n: int) -> list[list[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0               # 起始点
        loop, mid = n // 2, n // 2          # 迭代次数、n为奇数时，矩阵的中心点
        count = 1                           # 计数

        for offset in range(1, loop + 1) :      # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset) :    # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums

if __name__ == '__main__':
    n_1 = 3
    print(Solution_1().generateMatrix_1(n_1))
    n_2 = 1
    print(Solution_1().generateMatrix_1(n_2))
#=======================================================================================================================
print("*" * 50)
#=======================================================================================================================
# 定义四个边界
class Solution_2(object):
    def generateMatrix_2(self, n):     # PS:slef的作用与相关属性
        if n <= 0:
            return []

        # 初始化 n x n 矩阵
        matrix = [[0] * n for _ in range(n)]

        # 初始化边界和起始值
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # 从左到右填充上边界
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 从上到下填充右边界
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 从右到左填充下边界
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # 从下到上填充左边界
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
if __name__ == '__main__':
    n_1 = 3
    print(Solution_2().generateMatrix_2(n_1))
    n_2 = 1
    print(Solution_2().generateMatrix_2(n_2))

# 一入循环深似海，从此offer是路人

#=======================================================================================================================
# self  # PS:slef的作用与相关属性
'''
在Python中，`self`是一个约定俗成的名称，用于在类的方法中引用类的实例。它允许方法访问和修改实例的属性和其他方法。

### `self`的作用
1. **访问实例属性**：通过`self`，方法可以访问和修改实例的属性。例如，`self.attribute`可以用来获取或设置实例的`attribute`属性。
2. **调用其他方法**：通过`self`，方法可以调用同一个类中的其他方法。例如，`self.other_method()`可以调用实例的`other_method`方法。
3. **引用实例本身**：`self`可以用来引用实例本身，这在需要将实例作为参数传递给其他方法或函数时非常有用。

### 示例
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

    def increment_value(self):
        self.value += 1

# 创建一个MyClass的实例
obj = MyClass(10)

# 调用print_value方法
obj.print_value()  # 输出: 10

# 调用increment_value方法
obj.increment_value()

# 再次调用print_value方法
obj.print_value()  # 输出: 11
```
'''

# 在这个示例中，`self`用于访问和修改`value`属性，以及调用`print_value`和`increment_value`方法。
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

    def increment_value(self):
        self.value += 1

# 创建一个MyClass的实例
obj = MyClass(10)

# 调用print_value方法
obj.print_value()  # 输出: 10

# 调用increment_value方法
obj.increment_value()

# 再次调用print_value方法
obj.print_value()  # 输出: 11
#  在这个示例中，`self`用于访问和修改`value`属性，以及调用`print_value`和`increment_value`方法。


