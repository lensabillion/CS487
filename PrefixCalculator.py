class stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    def push(self,toBePushed):
        self.size+=1
        self.stack.append(toBePushed)
        
    def pop(self):
        if len(self.stack)!=0:
            self.size-=1
            return self.stack.pop()
        else:
            return None
            
    def delete(self,toBeDeleted):
        for i in self.stack:
            if i==toBeDeleted:
                self.stack.remove(i)

    def top(self):
        if len(self.stack)!=0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def is_empty(self):
        return self.stack==[]
    
    def display(self):

        for i in self.stack:
            print(i,end=" ")
        print()
def preFix(expression):
    operators=stack()
    operand=stack()
    stackExp=stack()      
    digit = expression.split(" ")
    for i in digit:
        
        stackExp.push(i)
        
      
    while not stackExp.is_empty():
        if stackExp.top() != None:
            element =stackExp.pop()
         
            if element.isdigit():    
                operand.push(element)
            else:
                if element =="*":
                    num1 =int(operand.pop())
                    num2=int(operand.pop())
                    result =str(num1 * num2)
                    stackExp.push(result)
                elif element =="/":
                    num1 =int(operand.pop())
                    num2=int(operand.pop())
                    result =str(num1 / num2)
                    stackExp.push(result)
                elif element =="+":
                    num1 =int(operand.pop())
                    num2=int(operand.pop())
                    result =str(num1 + num2)
                    stackExp.push(result)
                elif element =="-":
                    num1 =int(operand.pop())
                    num2=int(operand.pop())
                    result =str (num1 - num2)
                    stackExp.push(result)
           
   
    operand.display()
    
preFix("+ 4 * 3 12")
        
            

