# num = int(input("eNTER NUMber"))
# fact = 1
# if num<0:
#     print("fact does not exist ")
# if num == 0:
#     print("fact of 0 is 1")
# if num>0:
#     for i in range(1,num+1):
#         fact = fact*i

# print('Ffcatoial ois', fact)


#######using recursiopn
def fact(a):
    if a == 0:
        return 1
    else:
        return((a)*fact(a-1))
num = int(input())
result = fact(num)
print(result)