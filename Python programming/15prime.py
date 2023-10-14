num = int(input())
if num == 1:
    print("1 is not a prime number")
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, " Not prime")
            break
    else:
        print(num, "is prime")