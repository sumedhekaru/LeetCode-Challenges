# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:09:25 2019

@author: Sumedhe Karunarathne
"""

"""
PROBLEM:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # this worked but take too much time for large inputs
        '''
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                tot = num1 + num2
                if i == j:
                    pass
                elif tot == target:
                    return [i, j]\
        '''
        
        
        # This dicttionary solution is much faster (because only has one for loop)
        dic = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff not in dic:
                dic[num] = i
            else:
                return[dic[diff], i]
                
                
                