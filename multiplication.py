def mult():
    firstnumber =input("enter the first number")
    secondnumber=input("enter the second number")
    negative=""
    if firstnumber=="0" or secondnumber=="0":
        return "0"
    if firstnumber[0]=='-' and secondnumber[0]=="-":
        negative=''
        firstnumber=firstnumber[1:]
        secondnumber=secondnumber[1:]
        
    elif firstnumber[0]=='-':
        negative="-"
        firstnumber=firstnumber[1:]
    elif secondnumber[0]=='-':
        negative='-'
        secondnumber=secondnumber[1:]
    
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
    
    mynum =[]
    while i >= 0 :
        total= ""
        carry =0
    
        for j in range(len(largernumber)-1,-1,-1):
            num1 = int(largernumber[j])
            num2 = int(smallernumber[i])
            mult = (num1*num2)+carry
            carry =mult// 10
            mult  = mult % 10
            total = str(mult)+total   
        if carry !=0:
            total = str(carry)+total
##        if negative == "":
##            mynum.append(total)
##        else:
##            total = "-" + total
##            mynum.append(total)
        mynum.append(total)
        i=i-1
    for i in range(0,len(mynum)):
        mynum[i]=mynum[i]+i*"0"
    sum="0"
    for i in range(0,len(mynum)):
        sum=sumOfPosetive(sum,mynum[i]) 
    for i in range (0,len(sum)-1):
        if sum[i]=="0":
            sum=sum[i+1:]
        break
    if negative=="-":
        
        print("-"+sum)
    
    else:
        
        print(sum)

def sumOfPosetive(firstnumber,secondnumber):

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
        
       

mult()
