# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:14:53 2022

my_solution = Solution()
my_solution.intToRoman(num)

@author: adrnna
"""
thisdict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
keyList=sorted(thisdict.keys())
multi = {1: 1, 2: 10, 3: 100, 4: 1000}
roman_out = []

class Solution(object):
    def intToRoman(self, num):
        ind = len(str(num))
        my_list = [int(x) for x in str(num)]
        roman_out = ""
        
        for each_digit in my_list:            
            if each_digit < 5:
                if each_digit != 4:
                    roman = thisdict[1*multi[ind]] * each_digit 
                else:
                    roman = thisdict[multi[ind]] + thisdict[keyList[(keyList.index(multi[ind]))+1]]
            else:
                 if each_digit != 9:
                     roman = thisdict[5*multi[ind]] + thisdict[multi[ind]] * (each_digit-5)
                 else:
                     roman = thisdict[multi[ind]] + thisdict[keyList[(keyList.index(multi[ind]))+2]]
            ind -= 1
            roman_out += roman    
        return roman_out
        
            
my_solution = Solution()

print(my_solution.intToRoman(3999))

