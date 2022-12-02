# # s='programming'
# # s1=s[::-1]
# # s2=s[::2]
# # print(s1,s2)

# s1 = 'abc'
# s2 = 'lmn'
# a = max(s1)
# b = min(s2)
# if a < b:
#     print(a, b)
# else:
#     print(c=0, d=2)


# def aps():
#     return['xyz', 700, -987]


# def say():
#     return 'abc', [42, 'python'], "raj"


# print(aps())
# print(say())

# s1=43;
# s2=1;
# s3='43';
# print(s1+s2)
# print(s3+s3)
# # print(s1+s3)

class child:
    def func1(self):
        print("this is function1")
        class parent(child):
            def func2(self):
                print("this is function2")
                ob = child();
                ob.func1()
                ob.func2()