from math import sin
list = [1,2,3,4]
print("iterator")
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
#Iterator object can be traversed using regular for statement

print("max " + str(max(list)))

list1 = ['a','b','c','d']
print("max1 " + str(max(list1)))

list2 = ["aa","bb","cc"]
print("max2 " + str(max(list2)))

print("sin >> " + str(sin(0.523599))) #30 

print("for loop")
for x in it:
    print (x, end=" ")

print("\n while loop")
import sys
#using next() function
it1 = iter(list)
while True:
    try:
        print (next(it1))
    except StopIteration:
        #sys.exit() #you have to import sys module for this
        break;
        

print("#generator function")
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
        
        