largenow=-1
print('now large:',largenow)
for num in [45,22,16,92]:
    if num>largenow:
        largenow=num
    print(largenow, num)
print('the large num is ',largenow)
z=0
print('Now',z)
for new in [45, 21, 33, 51, 92]:
    z = z+new
    print(z,new)
print('now',z)

smalle=None
for value in [ 9, 45, 14, 3, 55]:
    if  smalle is None:
        smalle=value
    elif value < smalle:
        smalle=value
    print(smalle,value)
print('the smallest value: ', smalle)