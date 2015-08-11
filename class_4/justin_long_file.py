
def max_lines(*file_names):
    longest_file_name = ''
    longest_file_length = 0
    for file in file_names:
        with open(file, 'r') as f:
            lengthoffile = len(f.readlines())
            filename = str(file) #ahh ok you can not compare longest_file_length to length because it has no value
            #to me, it looks like it's not iterating. it does 1 file then stops
            # yea its not iterating. I have an idea
            if longest_file_length < lengthoffile:
                longest_file_name = filename
                longest_file_length = lengthoffile
    return longest_file_name
#THAT DID IT!
#Ah python, so infuriating yet so rewarding It is you reall have to watch spacing and never have def within def
#santi got on me about that. try in sis YES!!!!!!!! You are the man!

# it worked
print max_lines('tmp.txt','tmp2.txt', 'tmp3.txt')

'''
with open ('tmp.txt', 'r') as f:
    print f.readlines()
'''