import sys
import time

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1]=lst[j+1],lst[j]

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
    bubble_sort(lst)
    stop=time.clock()
    print("Time taken:",stop-start)
    print(lst)
    print("man")
    print('woman')
