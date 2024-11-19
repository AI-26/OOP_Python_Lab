n=int(input("choose 1:add \n 2:sub \n 3:div \n 4:mul \n"))
a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))
if(n==1):
    print(a+b)
elif(n==2):
    print(a-b)
elif(n==3):
    print(a/b)
elif(n==4):
    print(a*b)
else:
    print("invalid")