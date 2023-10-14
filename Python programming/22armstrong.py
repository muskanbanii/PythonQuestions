# # num = int(input())
# # sum = 0
# # temp = num
# # digit = temp %10 
# # cube = digit**3
# # sum= sum+cube
# # fd = temp//10


# num =  int(input())
# sum= 0
# temp=num
# while temp>0:
#     digit = temp%10  #3 #5
#     cube = digit**3 # 3x3x3 =8 #125
#     sum = sum+cube # 0+8 +125
#     temp //=10 #15
# if sum==num:
#     print(num, 'is armstrong number')
# else:
#     print("nooo")
num = int(input('enter the number: '))
order = len(str(num))
sum =  0
temp = num

while temp>0:
    digit = temp%10
    cube = digit**order
    sum = sum+cube
    temp //=10
if sum==num:
    print("Armstrong number")
else:
    print("Not a armstrong number")