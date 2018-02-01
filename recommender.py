
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#column headers for the dataset
data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date','video release date','IMDb URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance ','Sci-Fi','Thriller','War' ,'Western']
user_cols = ['user id','age','gender','occupation','zip code']

#importing the data files onto dataframes
users = pd.read_csv('./data/u.user', sep='|', names=user_cols, encoding='latin-1')
item = pd.read_csv('./data/u.item', sep='|', names=item_cols, encoding='latin-1')
data = pd.read_csv('./data/u.data', sep='\t', names=data_cols, encoding='latin-1')

# dataset = pd.merge(pd.merge(item, data),users)

R_df = data.pivot(index = 'user id', columns ='movie id', values = 'rating').fillna(0)
print(R_df)

# for index,row in R_df.iterrows():
#     print(row)
#     break
