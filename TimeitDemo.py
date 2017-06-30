import timeit

input_list=range(100)
'''
def divide_by(num):
    if num%5==0:
        return True
    else:
        return False

xyz=list(i for i in input_list if divide_by(i))

for i in xyz:
    print(i)

xyz=[i for i in input_list if divide_by(i)]

'''

##print(timeit.timeit('''input_list=range(100)
##def divide_by(num):
##    if num%5==0:
##        return True
##    else:
##        return False
##
##xyz=(i for i in input_list if divide_by(i))''', number=500))


print(timeit.timeit('''input_list=range(100)
def divide_by(num):
    if num%5==0:
        return True
    else:
        return False

xyz=(i for i in input_list if divide_by(i))
for i in xyz:
    x=i''', number=500000))
