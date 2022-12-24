#Program to print the fibonacci series
#Let n represent the number of values to be printed in fibonacci series
#Let fibonacci be the name of the list to store the fibonacci series
n=int(input("Enter the number of values to be printed in fibonacci series: "))
fibonacci=list(range(0,n))
if n<0:
    print("The input is incorrect")
elif n==0:
    print("The fibonacci series is: 0")
elif n==1:
    print("The fibonacci series is: 0,1")
else :
    fibonacci[0]=0
    fibonacci[1]=1
    print("The fibonacci series is: ")
    print("0")
    print("1")
    i=2
    while i<n:
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
        print(fibonacci[i])
        i+=1
    
         
    