import sys
import time
sys.setrecursionlimit(100000)


def quick_sort(lst,l,r):
    if(l<r):
        par=partition(lst,l,r)
        quick_sort(lst,l,par-1)
        quick_sort(lst,par+1,r)
def partition(lst,l,r):
    pivot=l
    r_boundary=r+1
    for i in range(r,l,-1):
        if(lst[i]>lst[pivot]):
            r_boundary=r_boundary-1
            lst[i],lst[r_boundary]=lst[r_boundary],lst[i]
    lst[pivot],lst[r_boundary-1]=lst[r_boundary-1],lst[pivot ]
    return r_boundary-1

if (__name__=='__main__'):
    choice=sys.argv[1]
    if(choice=='0'):
        file_name='data-sorted.txt'
    elif(choice=='1'):
        file_name='data-reverse.txt'
    elif(choice=='2'):
        file_name='data-random.txt'
    with open(file_name) as fo:
        lst=list(map(float,fo.readlines()))
    start=time.clock()
    quick_sort(lst,0,len(lst)-1)
    stop=time.clock()
    print("Time taken:",stop-start)
    print(lst)
    print("aman")
    print("aliya")
    print('rahul chutiya hai')
    print('makichu')
    print('mere bete')
    print("hello to the smallest chotu of our college")
    print('the smallest chotu of our college is ravi prakash')
                
