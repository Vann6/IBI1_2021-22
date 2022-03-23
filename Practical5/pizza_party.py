n=0
#Create a variable to record the number of slices.
cut=0
#Create a variable to record the number of cuts.
while n <64:
#Stop when there are enough slices for each member of IBI1 class.
    cut=cut+1
    n=(cut**2+cut+2)/2
#Calculate the number of slices.
    print("we have",str(n),"slices of pizza","by",str(cut),"cuts")
#Show the relationship between the number of cuts and slices.

print(str(cut),"cuts are required to make a slice for each member of the IBI1 class")
#Show the result.
#Eleven cuts are required to make a slice for each member of the IBI1 class
