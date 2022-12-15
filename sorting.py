def bubbleSort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def choice(array):
    l = len(array)
    for i in range(l-1):
        m = array[i]          # идем с лева на право от 0 элемента до конца
        id = i        # запоминаем индекс "минимального числа"
        for j in range(i+1,l):
            if m > array[j]:     # есть число меньше
                m = array[j]       # запоминаем его и его индекс
                id = j
        if id!=i:           # меняем их местами
            array[i],array[id] = array[id],array[i]
    return array
def insertion(array):
    l = len(array)
    for i in range(1, l):
            # идем от iтого элемента в обратную сторону и ищем элементы меньшие i-1того элемента
        if array[i] < array[i-1]:    # идем пока не найдем число меньше iтого
            array[i],array[i-1] = array[i-1],array[i] # меняем их местами
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

array = [3,100,50,60,33,-10,-20]
print(choice(array))
print(bubbleSort(array))
print(choice(array))
print(insertion(array))