#bubble sort: iterate through list, comparing each pair of adjacent elements, 
#swapping if necessary so that the lesser element is in front. At the end of each
#iteration, one or more elements has been placed correctly, beginning with the
#element.

#take a_list and swap elements i and j
def swap(a_list,i,j):
    tmp = a_list[i]
    a_list[i]=a_list[j]
    a_list[j]=tmp
    

def bubble_sort(a_list):
    #length of our list
    length = len(a_list)
    #i is our index, and the counter for our loop
    runagain = True

    while runagain:
        runagain = False
        for i in range(length-1):
            #compare element @ position i with element @ position i+1
            #if element i is greater than element i+1 then swamp positions using pop and insert functions.
            if a_list[i] > a_list[i+1]:
                #pop element i in temp
                tmp = a_list.pop(i)
                a_list.insert(i + 1,tmp)
                runagain = True
            #else: runagain = False

    return a_list
            
a_list = [8,3,10,2,1,7,22]
swap(a_list,0,1)