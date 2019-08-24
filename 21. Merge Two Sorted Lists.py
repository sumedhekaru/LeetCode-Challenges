# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:40:31 2019

@author: Dr Stolzenburg
"""

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def node2list(nodes):        
            x = nodes
            val = []
            while x is not None:
                val.append(x.val)
                x = x.next
               
            return val
        
        def list2node(li):
            
            if li == []:
                return ListNode('')
            
            x = ListNode(li[0])
            last = x
            
            for i in range(1,len(li)):
                #print(last)
                last.next = ListNode(li[i])
                last = last.next
                
                
            return x
                
        
        val1 = node2list(l1)
        val2 = node2list(l2)
        val3 = val1 + val2
        val3.sort()
        val3 = list2node(val3)
        return val3
        
        
        #print(list2node(val3))