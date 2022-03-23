a=19245301
#The total number of cases of COVID-19.(7 March, 2022)
b=4218520
#The total number of cases of COVID-19.(7 March, 2021)
c=271
#The total number of cases of COVID-19.(7 March, 2020)
d=b-c
#The difference between the number of cases in 2020 and 2021.
e=a-b
#The difference between the number of cases in 2021 and 2022.

if  d>e :
    print("The rate in 2020 is greater than that in 2021")
#Compare e and d. Because the differences are collected in one year.
#The diffences can directly reflect the rate size.
elif d<e : 
    print("The rate in 2021 is greater than that in 2020")
else:
    print("The rate in 2020 is same as that in 2021")
#Compare e and d. Because the differences are collected in one year.
#The diffences can directly reflect the rate size.

    
#The rate in 2021 is greater than that in 2020.
    
