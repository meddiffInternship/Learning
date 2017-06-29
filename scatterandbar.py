from matplotlib import pyplot as plt

x=[5,6,7,8]
y=[7,3,8,3]

x2=[5,8,4,1]
y2=[1,6,2,9]

#plt.scatter(x,y,color='c')

plt.bar(x,y,color='k')
plt.bar(x2,y2)

plt.title('Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
#plt.legend()
#plt.grid(True,color='r')

plt.show()
