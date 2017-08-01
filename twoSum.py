# find if target ==  sum of 2 numbers in array
#Two Sum problem

from __future__ import print_function
import sys

def isSum(target,arr):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while(low < high):
        if target > arr[low] + arr[high]:
            low += 1
        elif target < arr[low] + arr[high]:
            high -= 1
        else:
            return(arr[low],arr[high])

    return 0



if __name__ == '__main__':

    arr = []
    for x in range(input('Size of array ')):
        arr.append(input())
            
    target = int(raw_input('Enter Sum '))
    
    try:
        x,y = isSum(target,arr)
        print('Element is sum of ',x,y)
    except:
        print('Element not found')




