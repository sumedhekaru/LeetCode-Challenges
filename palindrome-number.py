# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:06:17 2019

@author: Sumedhe Karunarathne
"""

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        val = str(x)
        
        val2 = ''
        L = len(val)
        
        for i in range(L):
            val2 = val2 + val[L-i-1]

        if val2 == val:
            return True
        else:
            return False
        
    def isPalindrome2(self,x):
        # 2nd solution without using strings
         # if the number is negative this is never going to happen
        if x < 0:
            return False
        
        # if you come this far, x is positive
        
        y = 0
        val = x
        while x > 0:
            remainder = (x % 10)
            y = y*10 + remainder
            x = (x - remainder)/10


            #print x
            #print y
        
        #print y
        if y == val:
            return True
        else:
            return False
        
    def isPalindrome3(self,x):
        # one line solution
        return str(x) == str(x)[::-1]


print(Solution().isPalindrome(121)) # True
print(Solution().isPalindrome(-121)) # False
print(Solution().isPalindrome(10)) # False

print('==========================')
print(Solution().isPalindrome2(121)) # True
print(Solution().isPalindrome2(-121)) # False
print(Solution().isPalindrome2(10)) # False

print('==========================')
print(Solution().isPalindrome3(121)) # True
print(Solution().isPalindrome3(-121)) # False
print(Solution().isPalindrome3(10)) # False
