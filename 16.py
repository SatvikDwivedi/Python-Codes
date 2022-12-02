# sum = 0
# x = str(input("enter the string = "))
# print(len(x))

def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
    for i in range(N-M+1):
        j = 0
    while j < M:
        if(txt[i+j] != pat[j]):
            break
        j += 1
        if(j == M):
            res += 1
            j = 0
            return res


txt = input()
pat = input()
print(countFreq(pat, txt))
