marks=[45,36,86,57,53,92,65,45]
#Create a list of marks.
print(sorted(marks))
#Sort the values and show the values.
import matplotlib.pyplot as plt
#import module.

plt.boxplot(marks,
            patch_artist=True,meanline=True,
            showbox=True,showfliers=True,
            showmeans=True,notch=False)
plt.title('The boxplot for the marks')
#Create a boxplot to display the distribution of marks.
#Means and meanline are shown in the boxplot.
average=sum(marks)/len(marks)
#Calculate the average.
print('The average of the marks is',average)
if average < 60 :
#Compare the average with 60.
    print('Rob failed this ICA')
#If the average is smaller, then Rob failed the ICA.
else:
    print('Rob passed this ICA')
#If the average is not smaller than 60, then Rob passed the ICA.
plt.show()
#Show the boxplot.
#The average is 59.875, which is smaller than 60.
#It shows that Rob failed the ICA.


#I also wrote some pseudocodes to test whether each mark are higher than 60 one by one.
#Because I misunderstood the conditions to pass the ICA.
#I thought that each marks need to be higher than 60 to pass the ICA.

#i=1
#Create a variable i.
#while i <9:
    #mark=marks[i-1]

    #if mark < 60:
        #print('Rob failed this ICA')

        #break
    #else:
        #i=i+1

#else:
    #print('Rob passed this ICA')


