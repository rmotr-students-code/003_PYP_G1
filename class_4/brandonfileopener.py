"""
Write a function, that receives a path to a text file as first parameter and
a list of string as second one. The function should write each string in a new
line of the text file. If 5 strings are given in the list, the resulting file
should have 5 lines.

Example:
  write_lines('test-file.txt', ['hello', 'world'])

"""


def write_lines(filepath, list_of_strings):
    testfile = open(filepath, 'w')
    for x in list_of_strings:
        testfile.write(x + '\n')
    testfile.close()
    
    brandonFile = open('brandon.txt')
    info = brandonFile.read()
    brandonFile.close()
    print info

write_lines('brandon.txt', ['Brandon', 'S', 'James'])