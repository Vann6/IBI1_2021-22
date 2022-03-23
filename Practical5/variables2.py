x=True
print("When x is", str(x))
y=False
print("y is", str(y))
#Create two variables and store string variables.
#Show the variables of x and y.
w=x and y
print("Then w is", str(w))
#Create w variable and show the variable.
#Repeat the steps above and change the values of x and y to investigate how w changes.

x=True
print("When x is", str(x))
y=True
print("y is", str(y))
w=x and y
print("Then w is", str(w))



x=False
print("When x is", str(x))
y=False
print("y is", str(y))
w=x and y
print("Then w is", str(w))



x=False
print("When x is", str(x))
y=True
print("y is", str(y))
w=x and y
print("Then w is", str(w))



#results:
#When x=True and y=False, then w=False.
#When x=True and y=True, then w=True.
#When x=False and y=False, then w=False.
#When x=False and y=True, then w=False.
