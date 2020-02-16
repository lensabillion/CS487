def countingSort(arr,exp1):
    n=len(arr)
    count =[0]*(10)
    output =[0]*(n) 

    for j in range(0,n):
        index=(arr[j]//exp1)
        count[(index)%10]+=1
  
    for i in range(1,10): 
        count[i] += count[i-1] 
  
   
    i = n-1
    while i>=0: 
        index = (arr[i]//exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
   
        
def radixSort(arr):
    maximum=max(arr)
    exp = 1
    while maximum//exp > 0: 
        countingSort(arr,exp) 
        exp *= 10
        
    
print(radixSort([170,45,75,90,802,24,2,66]) )       
