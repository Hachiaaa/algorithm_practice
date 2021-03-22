import sys
sys.path.append("..")
sys.setrecursionlimit(1000000)
from utils.random_list import random_list
from utils.time_test import time_test

def merge(left,right):
    res=[]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while len(left)>0:
        res.append(left.pop(0))
    while len(right)>0:
        res.append(right.pop(0))
    return res


def _merge_sort(li):
    mid=len(li)//2
    left=li[0:mid]
    right=li[mid:len(li)]
    if len(left)>0 and len(right)>0:
        left_list = _merge_sort(left)
        right_list = _merge_sort(right)
        return merge(left_list,right_list)
    return merge(left,right)

@time_test
def merge_sort(li):
    _merge_sort(li)

li=random_list(1000000)
merge_sort(li)