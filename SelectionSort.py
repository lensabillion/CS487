import random
numbers=list(range(0,10000))
random.shuffle(numbers)


for i in range(0,len(numbers)):
  
    min_idx = i
    for j in range(i+1,len(numbers)):
        if numbers[min_idx] > numbers[j]:
            
            min_idx=j
    numbers[i],numbers[min_idx]=numbers[min_idx],numbers[i]   
print(numbers)
            
