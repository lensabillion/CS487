def reverse(num):
        """
        :type x: int
        :rtype: int
        """
        reverse =""
        
        if num < 0:
            num = num + (-2*num)
            while num >0:
                r = num%10
                reverse += str(r)
                num =num // 10
                
            num = int ("-" + reverse)
            print(num)
        else:
            if num == 0:
                return 0
            else:
                while num >0:
                    r = num%10
                    reverse += str(r)
                    num =num // 10
                num = int (reverse) * 1
        if((num)>(2**31)-1):
            return 0
        elif(num < (-2**31)):
            return 0
        else:
            return num
        print(num)
reverse(-123)
