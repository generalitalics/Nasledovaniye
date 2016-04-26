reqq = {}
n = int(input())
a = []
#Ввод и запись в словарь
for i in range(n):
    x=input().strip(':').split()
    if x[0] not in reqq:
        reqq[x[0]] = []
    if len(x)>1:
        reqq[x[0]].extend(x[2:])
#для одного ключа 
q = int(input())
for i in range(q):
    pred,duh = input().split()
        for k in range(10):
            duh_m=duh
                for j in range(len(reqq[duh_m])):
                        if pred in reqq[duh]:
                        a.append('Yes')
                            break
                    duh = reqq[duh_m][j]
