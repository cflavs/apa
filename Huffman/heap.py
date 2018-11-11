from node import *
def maxHeapify(arr, heap_size, index):

    biggest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < heap_size and arr[left] > arr[biggest]:
        biggest = left
    if right < heap_size and arr[right] > arr[biggest]:
        biggest = right
    if biggest!=index:
        arr[index],arr[biggest] = arr[biggest], arr[index]
        maxHeapify(arr,heap_size,biggest)
 
def minHeapify(arr, heap_size, index):

    smallest=index
    left = 2*index + 1
    right = 2*index + 2
    if left < heap_size and arr[left].freq < arr[smallest].freq:
        smallest = left
    if right < heap_size and arr[right].freq < arr[smallest].freq:
        smallest = right
    if smallest!=index:
        arr[index],arr[smallest] = arr[smallest], arr[index]
        minHeapify(arr,heap_size,smallest)

def buildHeap(arr,heap_size):
    for i in range(int(heap_size/2-1),-1,-1):
        #maxHeapify(arr,heap_size,i)
        minHeapify(arr,heap_size,i)

def heapSort(arr, heap_size):
    buildHeap(arr,heap_size)
    for i in range(heap_size-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        #maxHeapify(arr,i,0)
        minHeapify(arr,i,0)
def heapMinimum(arr,heap_size):
    return arr[0]
def heapExtractMin(arr, heap_size):
    if heap_size <1:
        return "heap underflow"
    min = heapMinimum(arr,heap_size)
    arr[0] = arr[heap_size-1]
    arr.pop()
    minHeapify(arr,len(arr),0)
    return min
def heapIncreaseKey(arr,index,key):
    if key < arr[index].freq:
        return "nada a ser feito"
    arr[index].freq = key
    while index>0 and arr[int((index-1)/2)].freq> arr[index].freq:
        arr[index], arr[int((index-1)/2)] = arr[int((index-1)/2)],arr[index]
        index = int((index-1)/2)
def heapInsert(arr,key,heap_size,father):
    arr.append(father)
    arr[heap_size].freq = -1
    heapIncreaseKey(arr,heap_size,key)