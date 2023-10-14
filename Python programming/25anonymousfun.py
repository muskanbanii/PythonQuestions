nterms = int(input())
result = list(map(lambda x : 2 ** x, range(nterms+1)))
for i in range(nterms+1):
    print("the value oof 2 to the power", i , 'is', result[i])