numbers =[12,11,13,5,6]

for i in range(1,len(numbers)):
    for j in range(0,i):
        if numbers[j] > numbers[i]:
            temp = numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp
    print(numbers)
            
