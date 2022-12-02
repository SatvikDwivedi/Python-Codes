# # # # # # # # x= str(input("enter the word = "))
# # # # # # # # def reverse(x):
# # # # # # # #   str = ""
# # # # # # # #   for i in x:
# # # # # # # #     str = i + str
# # # # # # # #   return str
# # # # # # # # print("the reversed word is = ")
# # # # # # # # print(reverse(x))
# # # # # # # l=[]
# # # # # # # for i in range(1000,2000):
# # # # # # #   if i%8==0 and i%5==0:
# # # # # # #     l.append(str(i))
# # # # # # # print(l,end="")

# # # # # # import random
# # # # # # x=random.randint(1,10)
# # # # # # y=0
# # # # # # while(x!=y):
# # # # # #   y=int(input("guess the number :"))
# # # # # # print("well guessed!!!")

# # # # # n=5
# # # # # for i in range(1,n+1):
# # # # #   for j in range(1,i+1):
# # # # #     print("* ",end="")
# # # # #   print("")
# # # # # for i in range(n-1,0,-1):
# # # # #   for j in range(i,0,-1):
# # # # #     print("* ",end="")
# # # # #   print("")

# # # # x=input("word :")
# # # # for i in range(len(x)-1,-1,-1):
# # # #   print(x[i],end="")
# # # # print("")

# # # x=str(input())
# # # cntd,cntl=0,0
# # # for i in x:
# # #   if i.isdigit():
# # #     cntd+=1
# # #   elif i.isalpha():
# # #     cntl+=1
# # # print(cntd)
# # # print(cntl)

# # class me:
# #   x=5
# #   print(x)
# # class printme():
# #   print(me())
# # me()
# import sympy as s
# x=s.Symbol('x')
# print(s.diff(s.sin(x)))