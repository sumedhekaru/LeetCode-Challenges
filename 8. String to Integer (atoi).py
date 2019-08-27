# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:58 2019

@author: Dr Stolzenburg
"""

class Solution:
    def myAtoi(self, str):
        
        L = len(str)
    
        start_index = float('inf')
        
        for c in '0123456789':
            temp = str.find(c)
            
            if temp != -1 and temp < start_index:
                start_index = temp
        
        # fix the negative sign
        #if start_index != 0 and str[start_index -1] == "-":
        #    sign = -1
        #else:
        #    sign = 1
        
        #print(start_index)
        # return zero for leading letters
        leading = str[0:start_index].strip()
        #print(leading)
        
        if leading == '-':
            sign = -1
        elif leading == '+':
            sign = 1
        else:
            return 0
                
        
        #print(start_index)
        
        if start_index + 10 > L:
            last_index = L
        else:
            last_index = L + 10
            
        # Fix the last index
        found = False
        counter = start_index
        
        while not found:
            try:
                x = int(str[counter])
                #print(x)
            except:
                last_index = counter
                found = True
            
            counter += 1
            
        
        #print(last_index)
        
        number =  int(str[start_index:last_index])
        
        if number > 2**31:
            number = 2147483648
    
        return number*sign
    
            
            
            
            
print(Solution().myAtoi('-25 758asdfsd'))