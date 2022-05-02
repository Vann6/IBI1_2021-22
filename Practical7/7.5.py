import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import some python libraries.

os.chdir('C:/cygwin/home/13016/IBI1_2021-22/Practical7')  # change the working directory.

covid_data = pd.read_csv("full_data(2).csv")  # import the actual data.

my_columns = [True, False, True, True, False, False]
China_new_data = covid_data.loc[covid_data['location'] == 'China', my_columns]
# Create an object that stores the data on new cases and deaths for China.

mean_new_cases = np.mean(China_new_data.iloc[:, 1])
mean_new_deaths = np.mean(China_new_data.iloc[:, 2])
print(mean_new_deaths)
print(mean_new_cases)
# they are different.
# around 35 people died in one day in average.
# around 894 people was infected the covid-19 in average.
# around 4% new cases that killed the infected person.

China_dates = covid_data.loc[covid_data['location'] == 'China', 'date']
China_new_cases = covid_data.loc[covid_data['location'] == 'China', 'new_cases']
China_new_deaths = covid_data.loc[covid_data['location'] == 'China', 'new_deaths']

plt.boxplot([China_new_deaths],
            patch_artist=True, meanline=True,
            showbox=True, showfliers=False,
            showmeans=True, notch=False,
            labels=['New deaths'])
plt.title("A boxplot for new deaths in China")
plt.show()
plt.boxplot([China_new_cases],
            patch_artist=True, meanline=True,
            showbox=True, showfliers=False,
            showmeans=True, notch=False,
            labels=["New cases"])
plt.title("A boxplot for new cases in China")
plt.show()
# plot the new cases and new deaths as a box plot.
# the mean values fit with what I get above.

data1 = plt.plot(China_dates, China_new_cases, 'b+',label="new cases")
data2 = plt.plot(China_dates, China_new_deaths, 'r+',label='new deaths')
plt.xlabel("Date")
plt.ylabel("Number")
plt.xticks(China_dates.iloc[0:len(China_dates):4], rotation=-90)
plt.title("The china new deaths and new cases over date")
plt.show()
# 'b+' means the china_new_cases are shown in blue dots in the plot.
# 'r+' means the china_new_deaths are shown in red dots in the plot.
# "plt.xticks(China_dates.iloc[0:len(China_dates):4], rotation=-90)" make the plot clearer by only including some data.
# it also presents the dates vertically on the x-axis
