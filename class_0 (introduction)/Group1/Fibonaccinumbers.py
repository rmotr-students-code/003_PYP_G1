# Take input of "nth" you want to get
# Ask if the function should be recursive or not
# inform user when number/string is invalid


def get_fib(nth):
    # 1 1 2 3 5 8 13 21 34
    x = 1
    y = 1
    for i in range(nth-1):
        # This works
        x,y = y,(x+y)
        
        # This doesn't return right values
        """
        x = y
        y = x + y
        """
    return x

#def get_fib_recursion(nth)
#    get_fib_recursion()
        
def get_nth():

    nth = None

    while True:

        try:
            nth = int(raw_input("What nth term do you want to get? "))

        except ValueError:
            print("Please enter an integer")
            continue

        else:
            break

    return nth

def get_recursive():

    recursive = None

    while (recursive != 'Y') or (recursive != 'N'):

        print("Do you want the program to be recursive?")
        recursive = str(raw_input("Please enter 'Y' for yes or 'N' for no: "))

        if (recursive == "Y") or (recursive == "N"):
            break
        else:
            print("Invalid input, please try again")

    return recursive


def main():

    nth = get_nth()
   # recursive = get_recursive()

    print get_fib(nth)

    #print "nth = {}".format(nth)
    #print "recursive = {}".format(recursive)


main()