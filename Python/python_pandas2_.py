import pandas as pd
data_1={
    'calories':[400,380,350],
    'duration':[50,40,45]
}
print(pd.Series(data_1,index=['Day1','Day2','Day3']))