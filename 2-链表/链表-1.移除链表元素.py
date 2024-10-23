# 链表-1.移除链表元素
'''
移除列表中所有等于target的节点
'''
#=======================================================================================================================
'''
# 学习来源
UP ：url = ‘https://space.bilibili.com/525438321’
视频：url = 'https://www.bilibili.com/video/BV18B4y1s7R9'
笔记：url = 'https://programmercarl.com/'
题目：url = 'https://leetcode.cn/problems/remove-linked-list-elements/description/'
'''
#=======================================================================================================================
'''
# 解题思路
# 传统方法思路 --- 不考虑虚拟头结点
while( head ！= None and head(0) = target): # 需要判断头结点是否为空
                                            # 为什么需要判断头节点是否为空呢： 因为要取头节点的值，如果为空，即相当于操作了空指针，编译就会报错
    head = head + 1
    cur = head
while (cur ！= None):
    if cur(0) = target:
        head = head + 1
    else:
        head = head + 1
    cur = cur + 1
return head
            
# 虚拟头结点 dummy head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next

'''
#=======================================================================================================================
'''
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 
示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
 

提示：
列表中的节点数目在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= val <= 50
'''
#=======================================================================================================================
# 解题
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next = head) #添加一个虚拟节点
        cur = dummy_head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next


# 接口
if __name__ == '__main__':
    head = [1,2,6,3,4,5,6]
    val = 4
    res = Solution().removeElements(head, val)

