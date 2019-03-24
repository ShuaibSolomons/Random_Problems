"""
# Author: Shu'aib Solomons
# Date: 24/03/19
# Description: The purpose of this is piece of code is to check if 2 words
# are anagrams of one another.
"""

#Takes in 2 strings and returns either True or False anagram or not 
def ana(left, right):
    if(len(left) != len(right)):
        return False
    left = sorted(left)
    right = sorted(right)
    for i in range (len(left)):
        if(left[i]!=right[i]):
            return False

    return True



################## Simple Test Case ##################
word1 = "cba"
word2 = "abc"

result = ana(word1,word2)

print(result)
