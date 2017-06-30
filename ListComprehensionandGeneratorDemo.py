'''#List comprhension
xyz=[i for i in range(10)]
print(xyz)

#generator
xyz=(i for i in range(10))
for i in xyz:
     print(i)
'''

input_list=[10,7,4,15,8,22,20,50,47]

def divide_by(num):
    if num%5==0:
        return True
    else:
        return False

xyz = (i for i in input_list if divide_by(i))
[print(i) for i in xyz]

xyz=[i for i in input_list if divide_by(i)]
#print(xyz)
[print(i) for i in xyz]

#embedding list comprehensions
for i in range(5):
   for ii in range(3):
       print(i,ii)

print('\n')

[[print(i,ii) for ii in range(3)] for i in range(5)]
     
