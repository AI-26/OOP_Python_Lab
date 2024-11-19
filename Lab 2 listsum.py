list=[]
size=int(input("enter size : "))
sum=0
for i in range(0,size):
    num=int(input())
    list.append(num)
for j in range(size):
    sum=sum+list[j]
print(sum)