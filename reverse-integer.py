# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:56:05 2019

@author: Sumedhe Karunarathne

"""

"""
Problem: 
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    
    def reverse(self, x: int) -> int:
        
        if abs(x) > 2**31-1:
            return 0
        
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        x = x*sign
        
        val = str(x)
        val2 = ''
        L = len(val)
        
        # print(L)
        for i in range(len(val)):
            # print(L-i-1)
            val2 = val2 + val[L-i-1]
        
        val3 = int(val2)
        
        if val3 > 2**31 -1:
            return 0
        else:
            return val3*sign
        


print(Solution().reverse(123))  # output: 321
print(Solution().reverse(-123)) # output: -321
print(Solution().reverse(120))  # output: 21