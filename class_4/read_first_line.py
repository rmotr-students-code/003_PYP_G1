import sys

def read_first_line(file_name, r):
    file = open(file_name)
    line1 = file.readline()
    line2 = file.readline()
    file.close()
    return line1

def read_first_line2(file_name):
    with open(file_name, 'r') as file:
        line1 = file.readline()
        return line1


print(read_first_line2(sys.argv[1]))