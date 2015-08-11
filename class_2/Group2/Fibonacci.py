
####################################################
#To do:
# - Add "recursive" functionality
# - Let user decide if recursive
# - Let user pick if Fib sequence starts with 0 or 1
# - Data validation. Program must inform the user   
#   when the number inserted is invalid
####################################################

# returns nth value if starting point is 0,1
def fib_zero(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

# returns nth value if starting point is 1,1
def fib_one(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
    
#recursive

def fib_recursive(n):
    pass    

# main function calls fib_zero and fib_one when user enters desired nth position
def main(n, start):
   try:
      n = int(raw_input('Enter integer nth term'))
   except ValueError:
      print "Invalid Option, only integers can be entered"
   
   start = int(raw_input("Enter start point, 0-1"))
  
   r = str(raw_input('Recurisve? Enter Y or N'))
   
   if start == 0:
      return fib_zero(n)
   elif start == 1:
      return fib_one(n)
   else:
      print "invalid start point, 0-1 are accepted"

########
#Testing
########

#Regular
assert main(1, 0) == 0, "Regular case failed"
assert main(1, 1) == 1, "Regular case failed"
assert main(10, 0) == 34, "Regular case failed"
assert main(10, 1) == 55, "Regular case failed"
assert main(33, 0) == 2178309, "Regular case failed"
assert main(33, 1) == 3524578, "Regular case failed"

#Input Validation
#assert main(a, 0) == , "Valid input case failed"
#assert main(a, 0) == , "Valid input case failed"