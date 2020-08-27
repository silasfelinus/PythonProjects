def find_even_index(arr):
    front_tally = 0
    back_tally = 0
    front_position = 0
    back_position = len(arr) - 1
    
    while front_position < len(arr):
        front_tally = front_tally + arr[front_position]
        back_tally = back_tally + arr[back_position]

        #troubleshooting
        print(front_tally)
        print(back_tally)
        #print(front_tally % 2 == 0)
        print(front_tally == back_tally)
        print(front_position)
        #print(back_position)

        if (front_tally % 2 == 0) & (front_tally == back_tally):
            print('here')
            return front_position + 1
        else:
            front_position += 1
            back_position -= 1
    return -1

print(find_even_index([1,2,3,4,3,2,1]))