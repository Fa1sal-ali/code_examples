# You are given an unsorted array with both positive and negative elements.
# You have to find the smallest positive number missing from the array in O(n) time using constant extra space. You can modify the original array.

# Examples 

#  Input:  {2, 3, 7, 6, 8, -1, -10, 15}
#  Output: 1

#  Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
#  Output: 4

#  Input: {1, 1, 0, -1, -2}
#  Output: 2

# Author: Faisal Ali
# Creation Date: 21-Jan-2021
# Version 1.0

class Solution:
    def smallestPos(self, arr):
        minInit = min(arr)
        maxInit = max(arr)
        lstInit = []
        lstFinal = []
        for elm in range(minInit,maxInit):
            if elm not in arr:
                lstInit.append(elm)
                
        if lstInit == []:
            return (maxInit+1)
        else:
            for i in range(len(lstInit)):
                if lstInit[i] > 0:
                    lstFinal.append(lstInit[i])

            return min(lstFinal)

obj = Solution()
arr = [1, 2, 0]
print(obj.smallestPos(arr))