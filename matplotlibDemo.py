from matplotlib import pyplot as plt

x=[5,6,7,8]
y=[7,3,8,3]

plt.plot(x,y,'c',linewidth=10,label='line one')

plt.title('Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='r')

plt.show()
