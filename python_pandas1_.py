import pandas
data_1={
    'Name' : 'Ram',
    'Age' : 20,
    'city' : 'karaikudi'
} 
print(pandas.DataFrame([data_1])) # This [] square bracket is very very important.
# Becasue Dataframs only accept the list or array values so it is important.

print(pandas.Series(data_1))