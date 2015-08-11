"""
Write a function, that receives one or many file paths as parameters and returns
the name of the file with max amount of lines.

Example:
  max_lines('file1.txt', 'file2.txt')  # 'file1.txt
  max_lines('file1.txt')  # 'file1.txt
  max_lines('file1.txt', 'file2.txt', 'file3.txt)  # 'file3.txt

"""


def max_lines(*file_names):
    linesofeachfilearray = []
    for x in file_names:
        with open(x) as f:
            count = 0
            for line in f:
                count+=1
            linesofeachfilearray.append(count)
    largestval = max(linesofeachfilearray)
    positionofarray = linesofeachfilearray.index(largestval)
    return file_names[positionofarray]

print max_lines('/home/ubuntu/workspace/class_4/tmp.txt','/home/ubuntu/workspace/class_4/tmp2.txt','/home/ubuntu/workspace/class_4/tmp3.txt')