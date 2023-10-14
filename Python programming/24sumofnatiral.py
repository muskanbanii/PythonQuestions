num=int(input("Enter the number: "))
if num<0:
    print("Please eneter natural number")
else:
    sum = 0
    while num>0:
        sum +=num
        num = num-1
    print(sum)
    