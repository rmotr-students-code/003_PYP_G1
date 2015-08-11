def bubblesort(a_list):
    print "original list " + str(a_list[:])
    done = False   
    
    while done == False:
        done = True
        for i in range(len(a_list)-1):
            if a_list[i] > a_list[i+1] :
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                done = False
    
    print "Sorted list " + str(a_list[:])
    print ""
    return a_list
########
#Testing
########
# Regular case
a_list = [7, 1, 13, 2, 27, 8]
assert bubblesort(a_list) == [1, 2, 7, 8, 13, 27], "Regular case failed"

# The largest one at the end
a_list = [7, 1, 13, 2, 27, 8, 94]
assert bubblesort(a_list) == [1, 2, 7, 8, 13, 27, 94], "Largest at end failed"

# The largest one at the start
a_list = [94, 7, 1, 13, 2, 27, 8]
assert bubblesort(a_list) == [1, 2, 7, 8, 13, 27, 94], "Largest at start failed"

# Other edge cases

a_list = [7, 1]
assert bubblesort(a_list) == [1, 7]

a_list = [1, 7]
assert bubblesort(a_list) == [1, 7]

a_list = [1, 1]
assert bubblesort(a_list) == [1, 1]

a_list = [1]
assert bubblesort(a_list) == [1]