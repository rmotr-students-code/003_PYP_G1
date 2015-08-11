"""
Write a function, that receives a path to two text files as parameters and copies
the content of the first file into the second, overwriting the content of the second
file if it's not empty.

Example:
  copy_file('test-file.txt', 'copy.txt')

"""
import os


def copy_file(source_file, target_file):

    if os.stat(source_file).st_size == 0:
        return "File not Empty"
    else:
        with open(source_file, 'r') as f:
            redirectfile = f.readlines()
            print redirectfile
            with open(target_file, 'w') as b:
               # b.write(redirectfile)
               for x in redirectfile:
                   b.write(x)
            return
        
        
copy_file('/home/ubuntu/workspace/class_4/hot.txt', '/home/ubuntu/workspace/class_4/output.txt')