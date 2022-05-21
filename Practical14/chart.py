import matplotlib.pyplot as plt
import numpy as np

list1 = [0, 1, 35, 0, 0, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 114, 8, 0, 0, 2, 0, 0, 3, 1, 0, 30, 0, 0, 1, 0, 0, 2, 2, 0, 67, 0, 0, 0, 0, 5, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 62, 2, 8, 0, 6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 110, 23, 19, 19, 0, 9, 0, 2, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 2, 11, 3, 0, 57]
list2 = [1, 2, 5, 2, 1, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 23, 403, 0, 86, 2, 31, 3, 4, 3, 1834, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 6, 0, 0, 0, 0, 27, 2643, 300, 300, 0, 1, 5, 0, 0, 4, 0, 0, 0, 7, 52, 0, 1, 6, 0, 0, 13, 2, 0, 2, 0, 3, 0, 0, 0, 3, 0, 0, 12, 11, 4, 3, 1, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 10, 2, 0]
# list1 contains the number of childNodes for first one hundred terms in GO
# list2 contains the number of childNodes for first one hundred terms that contains 'translation' in GO
plt.boxplot(x=[list1,list2],
            meanline=True, showmeans=False,
            patch_artist=True, showbox=True,
            showfliers=False, notch=False,
            labels=['terms', 'term that contains translation'])

plt.title("The boxplot of the number of childnodes")
plt.xlabel('The terms')
plt.ylabel("ylabel")
plt.show()

var1 = np.average(list1)
var2 = np.average(list2)
# compare the average numbers
if var1 > var2:
    print("the term contains translation have a smaller number of childNodes on average")
else:
    print("the term contains translation have a greater number of childNodes on average")

print(var1)
print(var2)

# the term contains translation have a greater number of childNodes on average