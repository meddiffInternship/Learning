
import pandas as pd
import numpy as np

##df = pd.read_csv('C:\\Users\\Anupama C\\Desktop\\file1.csv')
##print(df)
##
##print("Maximum temperature:")
##print(df['Temperature'].max())
##
##print('Days on which it rained')
##print(df['EST'][df['Events'] == 'Rain'])
##
##print('Average temperature:', df['Temperature'].mean())

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
#print(df)
print(df.head(2))
print(df.tail(3))

print(df.set_index('Day'))
#convert dataframe to python list
print(df.Visitors.tolist())
#convert dtaframe to numpy array
print(np.array(df[['Bounce_rate', 'Visitors']]))
