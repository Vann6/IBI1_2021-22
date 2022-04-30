import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import some python libraries.

os.chdir('C:/cygwin/home/13016/IBI1_2021-22/Practical7')  # change the working directory.

covid_data = pd.read_csv("full_data(2).csv")  # import the actual data.

my_columns2 = [True, False, True, True, False, False]
China_new_data = covid_data.loc[covid_data['location'] == 'China', my_columns2]
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

plt.boxplot(China_new_deaths,
            patch_artist=True, meanline=True,
            showbox=True, showfliers=False,
            showmeans=True, notch=False,
            labels=None)
plt.show()
plt.boxplot(China_new_deaths,
            patch_artist=True, meanline=True,
            showbox=True, showfliers=False,
            showmeans=True, notch=False,
            labels=None)
plt.show()
# plot the new cases and new deaths as a box plot.
# the mean values fit with what I get above.

plt.plot(China_dates, China_new_cases, 'b+')
plt.plot(China_dates, China_new_deaths, 'r+')
plt.show()
# 'b+' means the china_new_cases are shown in blue dots in the plot.
# 'r+' means the china_new_deaths are shown in red dots in the plot.
# plot the data over date.
