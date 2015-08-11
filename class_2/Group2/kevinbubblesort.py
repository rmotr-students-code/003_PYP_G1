def bubblesort(a_list):

    for n in range(len(a_list)-1,0,-1):
        for i in range(n):
            if a_list[i] > a_list[i+1]:
                #swap
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    return a_list

a_list = [8,1,2,3,4,5,6,7]
print bubblesort(a_list)