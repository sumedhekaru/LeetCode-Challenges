# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:58 2019

@author: Dr Stolzenburg
"""

class Solution:
    def myAtoi(self, str):

      # def myAtoi(self, str):
        
        str = str.strip()
        L = len(str)
        
        if L == 0:
            return 0
        
        if L == 1 and not str.isnumeric():
            return 0
        
        sign = 1
        
        # first character should be numeric if not return 0
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]
        elif not str[0].isnumeric():
            return 0
        
        num = ''
        
        #print(str)
        
        for i, c in enumerate(str):
            #print(c)
            if i > 10:
                    break
                
            if c.isnumeric():  
                num = num + c
            else:
                break
        
        try:
            num = int(num)*sign
        except ValueError:
            return 0
        #print(num)
        
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num
 

            
            
print(Solution().myAtoi('+-2'))