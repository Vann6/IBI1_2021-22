import os
import pandas as pd
import matplotlib.pyplot as plt
# Import some python libraries.
os.chdir('C:/cygwin/home/13016/IBI1_2021-22/Practical7')  # change the working directory.
covid_data = pd.read_csv("full_data(2).csv")  # import the actual data.


my_columns = [True, False, True, False, True, False]
dataframe_Spain = covid_data.loc[covid_data['location'] == 'Spain', my_columns]
print(dataframe_Spain)
# get the dataframe shows that new cases and total cases in Spain
Spain_dates = covid_data.loc[covid_data['location'] == 'Spain', 'date']
Spain_new_cases = covid_data.loc[covid_data['location'] == 'Spain', 'new_cases']
Spain_total_cases = covid_data.loc[covid_data['location'] == 'Spain', 'total_cases']
data1 = plt.plot(Spain_dates, Spain_new_cases, 'b+',label="new cases")
data2 = plt.plot(Spain_dates, Spain_total_cases, 'r+',label='total cases')
plt.xlabel("Date")
plt.ylabel("Number")
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4], rotation=-90)
plt.title("The spain new cases and total cases over date")
plt.show()
# Make a plot for new cases and total cases in Spain.

# The covid was quite dangerous. It started in March 2020. And developed rapidly.
# From March 2020 new case and total cases increased.
# At the end of March new case reached to about 10000 cases.
# And the total cases increased rapidly. At the end of March the total cases was more than 85000 cases.
