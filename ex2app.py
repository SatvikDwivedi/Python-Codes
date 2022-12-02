# Q1
var = input("enter a string: ")
var = var[::-1]
print(var)

# Q2
var = input("enter a string1: ")
var2=input("enter a string2: ")
print(var==var2[::-1])

# Q3
import random
var = int(input("enter a number: "))
for i in range (var):
    print(random.randint(0,1),end='')

# Q4
test_str = "gray, is best : color to ! girls ;"
print("the original string is : "+test_str)

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, "")
        print("The string after punctuation filter : "+test_str)

# Q5
x=(11, 2, 3, 14)
y=(13, 5, 22, 10)
z=(12, 2, 3, 10)
print("original list:")
print(x)
print(y)
print(z)
print("\nelement-wise sum of the said tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)

# Q6
L = [(),(),('',),('a','b'),('a','b','c'),('d')]
L = [t for t in L if t]
print(L)

# Q7
num = [10,20,30,(10,20),40]
ctr=0
for n in num:
    if isinstance(n,tuple):
        break
    ctr+=1
    print(ctr)

# Q8
from itertools import chain
tupleMat = [[(9,51),(7,9)],[(11,1),(22,19)]]
print("tuple matrix: "+str(tupleMat))
convertedTuple = list(zip(*chain.from_iterable(tupleMat)))
print("converted list of tuple: "+str(convertedTuple))

# Q9
input_list = [1,2,2,5,8,4,4,8]
l1 = []
count = 0
for items in input_list:
    if(items not in l1):
        count += 1
        l1.append(ele)
    print("no. of unique items are: ",count)

# Q10
def comb(L):

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
                comb([1, 2, 3])

# Q11
def is_even_num(l):
    enum = []
    for n in l:
        if n%2 == 0:
            enum.append(n)
            return enum
            print(is_even_num([1,2,3,4,5,6,7,8,9]))

# Q12
def ispalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
            left_pos += 1
            right_pos -= 1
            return True
            print(ispalindrome('str'))

# Q13
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
            return True;
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
                return True
                print(test_prime(6))