try:
    x = float(input('Enter Countdown: '))
except:
    print('error')
    quit()   

while(x > 0) :
    print (x)
    x = x - 1
print('ended')