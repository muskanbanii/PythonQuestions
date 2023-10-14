# for i in range(1,100):
#     if i % 13 ==0:
#         print(i)

L= [39,48,26,98,33,67,87]
result = list(filter((lambda x : x%13 == 0,L)))
print(result)