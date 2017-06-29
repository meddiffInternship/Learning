from matplotlib import pyplot as plt
import numpy as np

x,y=np.loadtxt('C://Users//Anupama C//Pictures//Saved Pictures//random.txt',
               unpack=True,delimiter=',')

plt.plot(x,y,color='k')

plt.title('Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
