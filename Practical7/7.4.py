import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir('C:/cygwin/home/13016/IBI1_2021-22/Practical7')  # change the working directory.
covid_data = pd.read_csv("full_data(2).csv")  # import the actual data.
dataframe1 = covid_data.head(5)
# create a new dataframe including the first five rows of the dataframe of covid data.
dataframe2 = covid_data.head(10)
# create a new dataframe including the first ten rows of the dataframe of covid data.

covid_data.info()
# show some information about the dataframe.
# there are 6 columns called date, location, new_cases, new_deaths, total_cases and total_deaths in the dataframe.
# data in the columns of date and location are object.
# data in the columns of new_cases, new_deaths, total_cases and total_deaths are integer.
# there are 7996 rows in the dataframe.

covid_data.describe()
# describe some values of the dataframe.
# the mean of new cases is 194.55.
# the standard deviation of new cases is 2083.40.
# the maximum of new cases is 65162.
# the minimum of new cases is -9. Why the number of new cases can be smaller than 0?

var1 = covid_data.iloc[0, 1]
# the output is 'afghanistan', in the first row and second column.
var2 = covid_data.iloc[2, 0:5]
# output the first row and the first five columns.

var3 = covid_data.iloc[0:2, :]
# output the first two rows the entire columns.
var4 = covid_data.iloc[0:10:2, 0:5]
# output the first ten row with an interval value two and the first five columns.
var5 = covid_data.iloc[10:21, [0, 2]]
print(var5)
# output the 10-20 rows and first and third columns.

my_columns = [True, True, False, True, False, False]
var6 = covid_data.iloc[0:3, my_columns]
# output the first three rows and the columns whose corresponding value is true.

# my_columns = [True, True, False, True, False]
# if one value is deleted, which means my_columns is shorter than the number of columns of the dataframe.
# or if one value is added, which means my_columns is longer than the number of columns of the dataframe.
# then it will tell you there is an error in the codes.
# var = covid_data.iloc[0:3, my_columns]

var7 = covid_data.loc[2:4, 'date']
# show the data in the from 2 to 4 rows and column for date.

my_columns = [False, False, False, False, True, False]
dataframe_Afghanistan = covid_data.loc[covid_data['location'] == 'Afghanistan', my_columns]
print(dataframe_Afghanistan)
# use a Boolean to show "total_cases" for all rows corresponding to Afghanistan.
# we can also get the same dataframe by type dataframe_Afghanistan = covid_data.loc[0:81, 'total_cases']


