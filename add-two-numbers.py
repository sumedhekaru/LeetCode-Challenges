# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:35:48 2019

@author: Sumedhe Karunarathne
"""

# Since the ListNode class is given, and not implmented here, the code cannot
# test outside LeetCode enviornoment, not unless you wrote your own ListNode class.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def convertToInt(li):
            x = li
            val = 0
            n = 0
            while x is not None:
                val = val + x.val*(10**n)
                x = x.next
                n+=1            
            return val
        
        def tolist(n):
            
            n = str(n)
            
            node =  ListNode(n[-1])
            last = node
            
            for i in range(len(n)-1):
                last.next = ListNode(n[-i-2])
                last = last.next
                
            return node
