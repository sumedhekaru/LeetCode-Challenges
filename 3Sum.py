# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:41:34 2019

@author: Sumedhe Karunarathne
"""
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""



# This solution worked, but not accepted as it exceeded the time limit. Need to
# improve this answer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        solstr = []
        
        nums.sort()
        L = len(nums)
        count = 0
        
        for i in range(L-2):
            for j in range(i+1,L-1):
                for k in range(j+1,L):                    
                    if nums[i]+nums[j]+nums[k] == 0:
                        vec = [nums[i],nums[j],nums[k]]
                        #print(vec)
                        if sol == []:
                            sol.append(vec)
                            solstr.append(str(vec))
                            count += 1
                        else:
                            found = False
                            
                            for s in solstr:
                                if s == str(vec):
                                    found = True
                            
                            if not found:
                                sol.append(vec)
                                solstr.append(str(vec))
                                count += 1
                           
        return sol
                        