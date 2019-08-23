# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:43:02 2019

@author: Sumedhe Karunarathne
"""

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        L = len(s)
        maxL = len(s)
        
        def subStr(s1,L,maxL):    
            for i, c in enumerate(s1):
                ind = s1.find(c)
                
                if ind > -1:
                    s1 = s1[i:ind]
                    L = len(s1)
                else:
                    return L
        
        L = subStr(s,L,maxL)
        return L

print('Solution is:')
print(Solution().lengthOfLongestSubstring("abcabcbb")) # answer 3 