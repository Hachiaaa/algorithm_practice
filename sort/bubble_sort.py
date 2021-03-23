import sys
sys.path.append("..") # add utils directory into python system path
import utils.utils as util

def swap(li,i,j):
    li[i],li[j]=li[j],li[i]

@time_test
def bubble_sort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-1-i):
            if(li[j]>li[j+1]):
                util.swap(li,j+1,j)

li = util.random_list(1000000)

bubble_sort(li)



