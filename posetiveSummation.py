def sumOfPosetive():
    firstnumber =input("enter the first number")
    secondnumber=input("enter the second number")
    if len(firstnumber)<len(secondnumber):
        smallernumber = firstnumber
        largernumber = secondnumber
    else:
        smallernumber =secondnumber
        largernumber = firstnumber
    i=len(largernumber)-1
    digit_difference=len(largernumber)-len(smallernumber)
    if len(largernumber)-digit_difference>0:
        for j in range(0,digit_difference):
            smallernumber = "0" +smallernumber
    
    total= ""
    carry =0
    summation = 0
    while i >= 0 :
        
        num1 = int(largernumber[i])
        num2 = int(smallernumber[i])
       
        summation = num1+num2+carry
        carry =summation // 10
        summation  = summation % 10
        total =str(summation)+total
        i=i-1
      
    if carry!=0:
       
        total = str(carry)+total
    
    return total
        
       
print(sumOfPosetive())
