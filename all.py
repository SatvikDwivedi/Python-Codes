# print("Ans1")
# for i in range(1000,2001):
#     if(i%8==0 and i%5==0):
#         print(i,end=" ")
# print()

print("Ans 2")
num=5;
while(True):
    print("Guess the number")
    a=int(input())
    if(a==num):
        print("Well guessed")
        break
print()

print("Ans 3")
i=1
for i in range(6):
    j=1
    for j in range(i):
        print("*",end="")
    print()
for a in reversed(range(0,5)):
    for b in range(a):
        print("*",end="")
    print()
print()

# print("Ans 4")
# a=input("Enter the string: ")
# print(a[::-1])
# print()

# print("Ans5")
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)
# print()

# print("ans6")
# string=input("Enter the string: ")
# l=d=0
# for i in string:
#     if i.isdigit():
#         d=d+1
#     if i.isalpha():
#         l=l+1
# print("letters ",l)
# print("Digit",d)
# print()

# print("Ans 7")

# # Python program to check validation of password
# # Module of regular expression is used with search()
# import re

# password=input("Enter your password: ")
# flag = 0
# while True:
#     if (len(password) < 8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break

# if flag == -1:
#     print("Not a Valid Password")
# print()
# print("Ans 8")
# items = []
# for i in range(100, 401):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#         items.append(s)
# print( ",".join(items))
# print()


# print("Ans 10")
# num1=int(input("Enter num 1: "))
# num2=int(input("Enter num 2: "))
# if(num1+num2>105 and num1+num2<200):
#     print("200")
# else:
#     print(num1+num2)
# print()

# print("Ans 11")
# for i in range(9,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# print()

# print("Ans 12")
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
# print("Enter the length of 4 bars: ")
# histogram([int(input()), int(input()), int(input()), int(input())])
# print()

# print("Ans 13")
# num1= int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# if(num1!=num2):
#     if(abs(num1-num2)!=5):
#         print("false")
#     else:
#         print("true")
# else:
#     print("true")
# print()

# print("Ans 14")
# x1=int(input("enter x1 : "))

# x2=int(input("enter x2 : "))

# y1=int(input("enter y1 : "))

# y2=int(input("enter y2 : "))

# result= ((((x2 - x1 )*2) + ((y2-y1)*2) )*0.5)

# print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)
# def checkIfDuplicates_1(listOfElems):
#     if len(listOfElems) == len(set(listOfElems)):
#         return False
#     else:
#         return True
# listOfElems = []
# for i in range(5):
#     x=input()
#     listOfElems.append(x);
# if(checkIfDuplicates_1(listOfElems)==True):
#     print("duplicates found")
# else:
#     print("Duplicates not found")