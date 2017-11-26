import time

print ("time.localtime() >>" + str(time.localtime()))
print ("time.time() >>" + str(time.time()))
print ("time.asctime( time.localtime(time.time())) >>" + str(time.asctime( time.localtime(time.time()))))
print ("time.asctime( time.localtime()) >>" + str(time.asctime( time.localtime())))
print ("time.timezone >>" + str(time.timezone))
time.sleep(5)

import calendar

cal = calendar.month(2016, 2)
print ("\nHere is the calendar:")
print (cal)



