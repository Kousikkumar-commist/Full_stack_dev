import pandas as pd
import numpy as np
#name=np.dtype([('kousik',np.int8)])
#print(pd.Series(name,index=['x','y','z'])) # To change the index value 
details={
    'name':'kousik',
    'age':16,
    'city':'kolkata',
    'country':'india'
}
print(pd.Series(details))
print(pd.DataFrame(details,index=['Day1','Day2']))
'''import pandas as pd

details = {
    'name': 'kousik',
    'age': 16,
    'city': 'kolkata',
    'country': 'india'
}
print(pd.DataFrame(details))

# Create a pandas DataFrame from the details dictionary
dfill = pd.DataFrame([details])


# Access the first row using.loc
print(dfill.loc[0],'\n\n')'''
