paternal_age=[30,35,40,45,50,55,60,65,70,75]
#Create a list of fathers' age.
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#Create a list of the relative risk for congenital heart disease in the offsprings.
#These data was obtained from Supplementary Table 1 of the following paper:'Paternal-age-related de novo mutations and risk for five disorders',PMID:31292440.
Data=dict({30:1.03,
          35:1.07,
          40:1.11,
          45:1.17,
          50:1.23,
          55:1.32,
          60:1.42,
          65:1.55,
          70:1.72,
          75:1.94})
#Create a dictionary for two lists.
print(Data)
#Show the dictionary that records all the data.
x=30
#The valeue of x can be modified.
print(Data[x])
#Show the relative risk of congenital heart disease for a offspring with a 40-year-old father.
import matplotlib.pyplot as plt
#Import module.

x=paternal_age
y=chd
plt.scatter(x,y,color='red')
plt.plot(x,y)
#Create a scatter plot with age on the X-axis and chf on the Y-axis.
#Show all the data points with red dots.
plt.xlabel("Fathers' age")
plt.ylabel("The relative risk of congenital heart disease")
plt.title("The relationship between fathers's age and relative risk of chd")
#Create a title for the plot and labels for axises.
plt.show()
#Show the plot.

