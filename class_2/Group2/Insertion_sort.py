def insertionSort(a_list):
    #iterate the list
    for i in range(1,len(a_list)):
        currentvalue = a_list[i]
        index = i
    
    while index>0 and a_list[index-1]>currentvalue:
        a_list[index]=a_list[index-1]
        index = index-1
        
    a_list[index]=currentvalue
    print a_list

a_list = [54,26,93,17,77,31,44,55,20]
insertionSort(a_list)
