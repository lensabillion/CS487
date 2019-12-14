def divide():
    w = int(input())
    if isEven(w):
        if w!=2:
            print("yes")
        else:
            print("No")

                
    else:
        print("No")

def isEven(num):
    if num % 2 ==0:
        return True
divide()
            
