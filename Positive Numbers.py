"""
Created on Sat Dec 24 18:02:53 2022

@author: SANJANA
"""
#Program to print the positive values in range from a list of values
#Let n represent the number of values in the list
#Let numbers be the name of the list containing the values
n=int(input("Enter the number of values to be entered in the list"))
numbers=list(range(0,n))
if n<0 or n==0:
    print("The input is incorrect")
else:
    i=0
    while i<n:
        numbers[i]=float(input("Enter the value"))
        i+=1
q=0
print("The positive values in the given list of values are:")
while q<n:
    if numbers[q]>0:
        print(numbers[q])
    q+=1
    
            