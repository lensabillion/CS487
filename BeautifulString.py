##https://codeforces.com/contest/1265/problem/A
num=int(input())
List=[]
mark=["a","b","c"]
for i in range(0,num):
    string=input()
    List.append(string)
for val in List:
    beauty=""
    for i in range(0,len(val)-1):
        if val[i] != '?' and val[i]==val[i+1]:
            beauty = beauty + "-1"
            break

    if len(beauty)==0:   
        for i in range(0,len(val)):
            if i == 0:
                prev = '?'
            else:
                prev=beauty[i-1]
            current =val[i]
            if i == len(val)-1:
                nextStr ='?'
            else:
                nextStr=val[i+1]

            if current!='?':
                beauty = beauty + current
            else:
                counts = [0,0,0]
                if prev != '?':
                    counts[ord(prev)-ord('a')]+=1
                if nextStr != '?':
                    counts[ord(nextStr)-ord('a')]+=1
                for j in range(0,3):
                    if counts[j] == 0:
                        beauty = beauty + chr(ord('a') + j)
                        break
    print(beauty)

                
            
