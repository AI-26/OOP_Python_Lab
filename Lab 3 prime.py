n=int(input("enter a number"))
num=n
count=0
for i in range(1,num//2+1):
    if(num%i==0):
        count+=1
if(count>1):
    print(f"{n} is not prime")
else:
    print(f"{n} is prime")