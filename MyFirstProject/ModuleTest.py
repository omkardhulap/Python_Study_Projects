# Function definition is here
def changval( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function 1: ", mylist)
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function 2: ", mylist)
    return