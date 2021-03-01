from typing import List

def bubble_sort(array:List[int])->List[int]:
    for i in range(1,len(array)):
        for j in range(0,len(array)-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]= array[j+1],array[j]
# O(n^2), 버블정렬, 비효율적

def quick_sort(A,lo,hi):
    def partition(lo,hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right]<pivot:
                A[left],A[right] = A[right],A[left]
                left+=1
        A[left],A[hi] = A[hi],A[left]
        return left

    if lo<hi:
        pivot = partition(lo,hi)
        quick_sort(A,lo,pivot-1)
        quick_sort(A,pivot+1,hi)
# 퀵정령은 빠르고 효율적이지만 최악의 경우 O(n^2)  병합정렬은 항상 일정한 성능을 보인다.

#안정정렬 - > 중복된 값을 입력 순서와 동일하게 정렬한다.