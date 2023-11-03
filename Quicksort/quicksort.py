def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivo = array[0]
        smaller_numbers = [i for i in array[1:] if i <=  pivo]
        bigger_number = [i for i in array[1:] if i > pivo]
        return (quicksort(smaller_numbers)) +  [pivo] + (quicksort(bigger_number))

array = [ 4, 6, 6, 33, 60, 2, 10, 9]    
print (quicksort(array))



def bubblesort(array, n):
    aux = 1
    while(aux):
        aux = 0
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                aux =  1

    return array
arr = [1, 33, 11, 22, 9, 0, 34, 12]
bubble = bubblesort(arr, len(arr) )
print(bubble)

             

