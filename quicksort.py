def partition(array,low,high):
    
    pivot = array[high]
    
    i = low - 1 #pointer for pivot element rightmost
    
    for j in range(low,high):
        if array[j] <= pivot:
            i = i + 1
            #swapping ith element with jth element
            array[i],array[j] = array[j],array[i]
    
    #swapping the greatest element at ith with pivot
    array[i+1],array[high] = array[high],array[i+1]
    print(array)
    return i+1
    
    
    
def quicksort(data,low,high):
    if low < high:
        pi = partition(data,low,high)
        
        #first half left pivot
        quicksort(data,low,pi-1)
        #second half right pivot
        quicksort(data,pi + 1,high)
        

data = [12,42,3,2,5,22]
print(data)
size = len(data)

quicksort(data,0,size-1)

print('Sorted Array')
print(data)
