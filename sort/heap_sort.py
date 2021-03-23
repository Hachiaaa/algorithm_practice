import sys
sys.path.append("..")
import utils.utils as util


def sift_down(li,low,high):
    tmp = li[low]
    i = low # parent pointer
    j = 2*i + 1 # child pointer
    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            break
    li[i] = tmp

@util.time_test
def heap_sort(li):
    n = len(li)
    for i in range(n//2,-1,-1):
        sift_down(li,i,n-1)
    for j in range(n-1,0,-1):
        util.swap(li,0,j)
        sift_down(li,0,j-1)

li = util.random_list(1000000)
heap_sort(li)


