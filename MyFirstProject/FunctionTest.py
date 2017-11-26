# Function definition is here
def changval( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function 1: ", mylist)
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function 2: ", mylist)
    print(globals())
    print(locals())
    return

# Now you can call changeme function
mylist = [10,20,30]
changval( mylist )
print ("Values outside the function: ", mylist)

print(globals())
print(locals())


# Function definition is here
def changref( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function before change: ", mylist)
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
changref( mylist )
print ("Values outside the function: ", mylist)


Money = 2000
def AddMoney():
    # Uncomment the following line to fix the code:
    global Money
    Money = Money + 1

print (Money)
AddMoney()
print (Money)