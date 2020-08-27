def find_even_index(arr):
    position = 0

    while position < len(arr):
        #print("F: " + str(sum(arr[:position])))
        #print("B: " + str(sum(arr[position + 1:])))
        if sum(arr[:position]) == sum(arr[position + 1:]):
            return position
            break
        else:
            position += 1

    return -1



#Tests
print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))