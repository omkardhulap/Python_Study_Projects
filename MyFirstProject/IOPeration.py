def readFile(file):
    #fo = open(file, "a")
    fo = open(file, "w")
    print ("Name of the file: ", fo.name)
    #print ("Closed or not : ", fo.closed)
    print ("Opening mode : ", fo.mode)
    fo.write( "Python is a great language but .\nYeah I am great!!\n");
    # Close opend file
    fo.close()
    
    
file = "D:\\Users\\omkar.d\\Desktop\\Goclipse_Installation_Error.txt";
readFile(file)

import os
#os.rename(file,"D:\\Users\\omkar.d\\Desktop\\Goclipse_Installation_Error_1.txt" )
print (os.getcwd())