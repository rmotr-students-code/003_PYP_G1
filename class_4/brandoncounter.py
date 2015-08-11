"""
Write a function, that receives the path to a text file that contains JUST ONE word
per line, and returns a dictionary with the counter of words starting with each
letter from 'a' to 'z'.

Example:
  counter_by_letter('words.txt')  
  # {
    'a': 2,
    'b': 10,
    'c': 0,
    ...
    'z': 1
  }

"""



def counter_by_letter(filepath):
    masterlist = []
    letterlist = []
    finaldict = {}
    with open(filepath) as f:
        fileme = f.readlines()
        for x in fileme:
          letterlist.append(x[0])
        for i in range(97,123):
          finaldict[chr(i)] = letterlist.count(chr(i))
    return finaldict
        


print counter_by_letter('/home/ubuntu/workspace/class_4/words.txt')
    