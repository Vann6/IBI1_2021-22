import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import some python libraries.

os.chdir('C:/cygwin/home/13016/IBI1_2021-22/Practical7')  # change the working directory.
os.getcwd()  # show the working directory.
os.listdir()  # show what files are in the working directory.

covid_data = pd.read_csv("full_data(2).csv")  # import the actual data.
print(covid_data)  # show the actual dataframe.

