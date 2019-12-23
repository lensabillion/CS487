###use Counting Sort###

s="car"
t="rat"
AS=[]
AT=[]
SC=""
TC=""
for k in range(0,len(s)):
    AS.append(s[k])
    AT.append(t[k])

for i in range(0,len(AS)):
    for j in range(0,i):
        if AS[j]>AS[i]:
            temp = AS[i]
            AS[i]=AS[j]
            AS[j]=temp
        if AT[j]>AT[i]:
            temp = AT[i]
            AT[i]=AT[j]
            AT[j]=temp
for i in range(0,len(AS)):
    SC =SC +AS[i]
    TC =TC +AT[i]
if SC == TC:
    print("true")
else:
    print("false")

