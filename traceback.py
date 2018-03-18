try:
    x = float(input('Enter X: '))
except:
    x = 'error'
    print('error')
    quit()   

if x > 10 :
    print('x is > 10')
else :
    print ('x is = or < 10')