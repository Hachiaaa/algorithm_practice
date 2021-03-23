import sys
sys.path.append("..") # add utils directory into python system path
import utils.utils as util

# partition function
def partition(li,low,high):
    tmp = li[low]
    left=low  #left pointer 
    right=high #right pointer
    while left<right:
        while left<right and li[right]>tmp:
            right -= 1
        li[left]=li[right]
        while left<right and li[left]<tmp:
            left += 1
        li[right]=li[left]
    li[left] = tmp # when loop is end,left pointer is equal to right pointer
    return left # return mid value index

def _quick_sort(li,low,high):
    if low < high:
        mid = partition(li,low,high)
        _quick_sort(li,low,mid-1)
        _quick_sort(li,mid+1,high)

@util.time_test
def quick_sort(li):
    left=0
    right = len(li)-1
    _quick_sort(li,left,right)



