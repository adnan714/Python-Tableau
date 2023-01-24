# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:07:19 2022

@author: dell
"""
import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep = ';')


data['CostPerTransation'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalePerTransation'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['profitPerTransaction'] = data['SalePerTransation'] - data['CostPerTransation']

data['Markup'] = data['profitPerTransaction'] / data['CostPerTransation'] 

#rounding the makup value

roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

# Combining Data Fields

print(data['Day'].dtype)

day = data['Day'].astype(str)
print(day.dtype)

my_date = day + '-' + data['Month']

year = data['Year'].astype(str)

my_date = day + '-' + data['Month'] + '-' + year

print(data['Year'].dtype)

data['date'] = my_date 

# using iloc to view specific columns/rows


 
 #using split to split the client keywords field
 #new_var = column.str.split('sep', expand = true)
 
split_col = data['ClientKeywords'].str.split(',' , expand = True)
 
# creaing new column fir the split column in client keyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#Using lower function to change item to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to merge files
# Bringing new data set

season = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merging file : merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, season, on = 'Month')

# Dropping Columns

#df = df.drop('columnname', axis =1)
data = data.drop('ClientKeywords', axis =1)
data = data.drop('Month', axis =1)
data = data.drop('Day', axis =1)
data = data.drop('Year', axis =1)

# Export into CSV

data.to_csv('ValueInc_cleaned.csv', index = False)


















