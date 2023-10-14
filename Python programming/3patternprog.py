#we have used two loops such that first one is for soaces and second is for stars
num= int(input())
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()
    