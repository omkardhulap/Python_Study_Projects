print("hello omkar!!")


count = 0
while count < 5:
    print (count, " is  less than 5")
    count += 1
else:
    print (count, " is not less than 5")
   

list = [1,2,3,4,5]

for i in list :
    print (i, " is  less than 5")
    i += 1
else:
    print (i, " is not less than 5") 

for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
    print()
  
while True :  # This constructs an infinite loop
    num = int(input("Enter a number  :"))
    #str = int(raw_input("Enter your input: "));
    print ("You entered: ", num)

print("hello omkar again!!")

