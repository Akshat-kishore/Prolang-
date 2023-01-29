# cook your dish here
I = int(input())
for i in range(I):
    x,y,A1,B1,A2,B2=map(int,input().split())
    if (A1==x or A1==y) and (B1==y or B1==x):
        print("1")
    elif (A2==x or A2==y) and (B2==y or B2==x):
        print("2")
    else:
        print("0")
