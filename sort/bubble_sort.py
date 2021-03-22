import sys
sys.path.append("..") # add utils directory into python system path
from utils.time_test import time_test
from utils.random_list import random_list

def swap(li,i,j):
    li[i],li[j]=li[j],li[i]

@time_test
def bubble_sort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-1-i):
            if(li[j]>li[j+1]):
                swap(li,j+1,j)

li = random_list(1000000)

bubble_sort(li)



