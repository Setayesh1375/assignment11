class fraction:
    def __init__(self , ss, mm):
        #properties
        self.s = ss
        self.m = mm

    #method    
    def sum(self , f1):
        s = self.s * f1.m + self.m * f1.s
        m =self.m * f1.m

        x=fraction(s,m)
        return x


    def mul(self , f1 ):
        result_s = f1.s * self.s
        result_m = f1.m * self.m

        x = fraction(result_s ,result_m)
        return x


    def sub(self , f1):
       s = self.s*f1.m-f1.s*self.m
       m = self.m*f1.m
       x = fraction(s, m)
       return x
    

    def div(self , f1):
       s=self.s*f1.m
       m=self.m*f1.s
       x=fraction(s, m)
       return x
    


    def fraction_to_number(self):
       number=self.s/self.m
       return number

    def show(self):
        print(self.s ,"/" , self.m)



a = fraction(2,3)
a.show()
b = fraction(7,1)
b.show()

z = b.mul(a)
z.show()

w = a.sum( b)
w.show()

sub = b.sub(a)
sub.show()

div=b.div(a)
div.show()

number=b.fraction_to_number()
print(number)