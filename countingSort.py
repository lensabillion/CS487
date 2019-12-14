number =[3,5,8,1,4,7,2,3,8]

count =[]
output =[]
max = 0
for i in range(0,len(number)):
    if number[i] > max:
        max = number[i]

for i in range(0,max + 1):
    count.append(0)
for j in range(0,len(number)):
    count[number[j]] = count[number[j]] +1
for k in range(0,len(count)):
    for f in range(0,count[k]):
        output.append(k)
        

print(output)
