import codecademylib3

# Import pandas with alias
import pandas as pd
import numpy as np
# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())
# data type of fields 
print(census.dtypes)

#inspecting data Frame 
print(census['birth_year'].unique())
census['birth_year']=census['birth_year'].replace(['missing'],1967)
census['birth_year']=census['birth_year'].astype('int')
print(census['birth_year'].unique())
print(census.dtypes)

print(census["birth_year"].mean())

census['higher_tax']=pd.Categorical(census['higher_tax'],['Strongly disagree','disagree','neutral','agree','strongly agree'],ordered=True)

print(census.dtypes)
print(census['higher_tax'])

#One Hot Encoding 
mf=pd.get_dummies(data=census, columns=['marital_status'])
print(mf.head())