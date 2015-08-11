"""
Write a function, that receives a path to a text file as first parameter, a string and
an optional "ovewrite_all" boolean. If overwrite_all is false, the function should
append the string at the end of current content in the text file. If it's true, it should
clean the content in the file and write only given string.

Example:
  write_string('test-file.txt', 'this is the string', overwrite_all=False)

"""


def write_string(filepath, a_string, overwrite_all=False):
    if overwrite_all == False:
        with open(filepath, 'a') as f:
            f.write(a_string + '\n')
            return 
    else:
        with open(filepath, 'w') as f:
            f.write(a_string + '\n')
            return
        
        
write_string('/home/ubuntu/workspace/class_4/tmp.txt', 'HAHAHAHA', overwrite_all=False)
        