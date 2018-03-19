smallest = None
for value in [9,3,23,2,56,3,4,8]:
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print('now: ', smallest)
print('end')