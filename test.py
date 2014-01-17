#test.py
#mike and will byrne
#jan 16, 2014
#teaching will some basics of python
#wills first coding lesson
#the speed of computations
#this took
#from: 	start time: Thu Jan 16 22:04:38 2014
#to:		end   time: Thu Jan 16 22:04:44 2014
#or 6 seconds;
#man that is fast!

import time
import datetime
from datetime import date

now = time.localtime(time.time())
print "    start time:", time.asctime(now)

i = 1
print i
while i < 20000000:
	#print i
	j = i*10/4 + 200
	i = i + 1
print i
print j

now = time.localtime(time.time())
print "    end   time:", time.asctime(now)
