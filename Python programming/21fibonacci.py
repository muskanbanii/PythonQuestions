num =  int(input("Enter the number till where you want fibonacci series: "))
a = 0
b= 1
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)


# or 
# # Initialize the first two numbers in the Fibonacci sequence
# a, b = 0, 1

# # Print the first 11 numbers in the Fibonacci sequence
# for _ in range(11):
#     print(a)
#     a, b = b, a + b
