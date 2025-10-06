a=int(input())
hours=a//3600%24
minutes= a%3600//60
seconds= a%60
print ('{}:{02}:{:02}'. format(hours,minutes,seconds) )