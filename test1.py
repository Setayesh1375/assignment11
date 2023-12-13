
def sum(s1,m1,s2,m2):
    result_s=s1*m2 + s2*m1
    result_m= m1*m2
    return result_s,result_m

def mul(s1,m1,s2,m2):
    result_s= s1*s2
    result_m= m1*m2

    return result_s,result_m

def fraction_to_number(s1,m1):
    if m1 !=0:
        result = s1/m1
        return result
    else:
        return "cannot divide by zero"

a=2
b=0

c=7
d=1

x,y = mul(a,b,c,d)
print(x,y)

x,y = sum(a,b,c,d)
print(x,y)

z = fraction_to_number(a,b)
print(z)