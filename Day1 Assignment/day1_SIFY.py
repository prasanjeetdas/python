nmber = int(input("enter number"))
check = number%2==0

if(check):
    print('even: ',end=" ")
    for item in range(number,number+10,2):
        print(item,end=" ")
    print()
    print('odd: ',end=" ")
    for item in range(number+1,number+10,2):
        print(item,end=" ")
else:
    print('odd: ',end=" ")
    for item in range(number,number+10,2):
        print(item,end=" ")
    print()
    print('even: ',end=" ")
    for item in range(number+1,number+10,2):
        print(item,end=" ")
