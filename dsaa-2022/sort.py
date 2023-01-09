def bubbleSort(arr):   # 이미 정렬된 구조가 있으면 그 뒤는 생략하는 코드면 더 좋겠다.
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] # 이렇게 리스트 위치바꾸는 코드도 오케이
 
def selectionSort(A):
    for i in range(len(A)):
        min_idx = i # 제일 작은 값으로 가정
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2  
        left = unsorted_array[:mid]  
        right = unsorted_array[mid:]  

        merge_sort(left) # 다시 넣어줘서 다시 나누는 작업, 왼쪽 먼저 다 나눈후 그다음 오른쪽차례
        merge_sort(right) # 다시 넣어줘서 다시 나누는 작업

        i = j = k = 0
       
        while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    unsorted_array[k] = left[i]
                    i += 1
                else:
                    unsorted_array[k] = right[j]
                    j += 1
                k += 1
          
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1

def partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high]  

    for j in range(low, high):
        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print ("Sorted array is:{0}".format(arr))
arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print ("Sorted array is:{0}".format(arr))
arr = [64, 34, 25, 12, 22, 11, 90]
insertionSort(arr)
print ("Sorted array is:{0}".format(arr))
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print ("Sorted array is:{0}".format(arr))
arr = [64, 34, 25, 12, 22, 11, 90]
quickSort(arr,0,6)
print ("Sorted array is:{0}".format(arr))