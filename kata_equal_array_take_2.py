def find_even_index(arr):
    front_position = 0

    while front_position < len(arr):
        #print('FRONT_SUM: ' + str(sum(arr[:front_position-1])) + ' BACSUM:' + str(sum(arr[front_position:])))
        print('FRONT_POS: ' + str(arr[front_position]))
        if sum(arr[:front_position-1]) == sum(arr[front_position:]):
            return (front_position - 1)
        else:
            front_position += 1
    return -1   




#Tests
print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))