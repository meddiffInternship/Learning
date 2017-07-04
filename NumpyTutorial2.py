import numpy as np

a=np.array([[1,2,7],[3,4,8],[5,6,9]])
b=np.array([[8,7,3],[9,2,7],[1,7,8]])

print('Array shape:', a.shape)
print('In 1D: ', a.ravel())
print('Array Dimension:', a.ndim)
print('Sum of array elements:', a.sum())
print('Adding 2 arrays:', a + b)
print('Minimum element:', a.min())
print('Maximum element:', a.max())

#slicing
print('After array slicing:', a[:,1:3])

#iterating
for row in a:
    print(row)

print('Printing each element of the array after flattening it:')
for cell in a.flat:
    print(cell)

#stacking 2 arrays
print('Vertical stacking of arrays:', np.vstack((a,b)))
print('Horizontal stacking of arrays:', np.hstack((a,b)))

#splitting an array
c = np.arange(30).reshape(2, 15)
print('New array: \n', c)
result = np.hsplit(c,3)
print('Horizontal split')
print(result[0])
print(result[1])
print(result[2])

#indexing with boolean arrays
print('--------------------------------------------------------')
x = np.arange(12).reshape(3,4)
print(x)
y = x > 5
print(y)
x[y] = -1
print('--------------------------------------------------------')
print('Replacing true values with -1')
print(x)
