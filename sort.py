def bubbleSort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - 1):
            if array[j] > array[j + 1]:
                x = array[j]
                array[j] = array[j + 1]
                array[j + 1] = x
def selection_sort(array):
    for i in range(len(array) - 1):
        m = i
        for j in range(i + 1, len(array)):
            if array[j] < array[m]:
                m = j
        array[i], array[m] = array[m], array[i]
    return array
def insertion(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while array[j] > x and j >= 0 :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x
    return array
def insertion_binary(array):
    for i in range(len(array)):
        key = array[i]
        start, end = 0, i - 1
        while start < end:
            mid = start + (end - start) // 2
            if key < array[mid]:
                end = mid
            else:
                start = mid + 1
        for j in range(i, start + 1, -1):
            array[j] = array[j - 1]
        array[start] = key
    return array
def mergeSort(array):
    if len(array)==1:
        return array
    mid = (len(array) - 1) // 2
    left = mergeSort(array[:mid + 1])
    right = mergeSort(array[mid + 1:])
    result = merge(left, right)
    return result
def merge(left, right):
    lst = []
    i = 0
    j = 0
    while(i <= len(left) - 1 and j <= len(right) - 1):
        if left[i]<right[j]:
            lst.append(left[i])
            i+=1
        else:
            lst.append(right[j])
            j+=1
    if i>len(left)-1:
        while(j <= len(right) - 1):
            lst.append(right[j])
            j+=1
    else:
        while(i <= len(left) - 1):
            lst.append(left[i])
            i+=1
    return lst
def quicksort(array):
    left = 0
    right = len(array)
    quick(array, left, right)
def quick(array, left, right):
    if right - left > 1:
        m = partition(array, left, right)
        quick(array, left, m)
        quick(array, m + 1, right)
    return array
def partition(array, left, right):
    mid = array[left]
    i = left + 1
    j = right - 1
    while True:
        while (i <= j and array[i] <= mid):
            i = i + 1
        while (i <= j and array[j] >= mid):
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[left], array[j] = array[j], array[left]
            return j