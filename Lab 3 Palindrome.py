n=int(input("enter a number : "))
num=n
sum=0
while(num>0):
    d=num%10
    num=num//10
    sum=sum*10+d
if(n==sum):
    print("yes")
else:
    print("no")