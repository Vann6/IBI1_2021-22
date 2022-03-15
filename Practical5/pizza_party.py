n=0
cut=0
while n <64:
    cut=cut+1
    n=(cut**2+cut+2)/2
    print("we have",str(n),"slices of pizza","by",str(cut),"cuts")
print(str(cut),"cuts are required to make a slice for each member of the IBI1 class")
