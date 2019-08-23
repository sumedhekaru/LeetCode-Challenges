# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:12:31 2019

@author: Sumedhe Karunarathne
"""

"""

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

"""


class Solution:
    def countCharacters(self, words, chars):
        
        total = 0
        L1 = len(chars)
        
        for word in words:
            L2 = len(word)
            temp = chars
            for c in word:
                temp = temp.replace(c,'',1)
            
            # print(temp)
            
            if L1 - len(temp) == L2:
                total += L2
        
        return total


words = ["cat","bt","hat","tree"]
chars = "atach"

print(Solution().countCharacters(words,chars))  # Answer should be 6

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

print(Solution().countCharacters(words,chars))  # Answer should be 10

