from unittest import result


num=int(input("enter the number:"))
factorial=1
result=1
while factorial<=num:
    result=result*factorial
    factorial=factorial+1
print(result)    