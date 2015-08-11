#bubble sort: iterate through list, comparing each pair of adjacent elements, 
#swapping if necessary so that the lesser element is in front. At the end of each
#iteration, one or more elements has been placed correctly, beginning with the last
#element.

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


'''
8,3,10,2,1,7,22
3,8,10,2,1,7,22
  3,8,10,2,1,7,22
       3,8,2,10,1,7,22
             3,8,2,7,10,22
   '''


import unittest

class BubbleSortTestCase(unittest.TestCase):
    def test_sorts_ok_with_the_largets_value_at_the_end(self):
        a_list = [8,3,10,22,2,1,7,89]

        self.assertEqual(
            bubble_sort(a_list),
            [1, 2, 3, 7, 8, 10, 22, 89])
            
            