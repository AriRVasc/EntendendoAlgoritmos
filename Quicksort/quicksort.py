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
