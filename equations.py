def pow(base,exp):
    if base==0:
        return (0)    
    elif exp==0:
        return(1)
    elif exp>0:
        result=1
        while (exp>0):
            result = base*result
            exp=exp-1    
        return (result)
    else:
        result=1
        while (exp<0):
            result = base*result
            exp=exp+1    
        return (1/result)

def factorialFun(num):
    if num==0:
        return(1)
    else:
        factorial=1
        i=1
        while (i<=num):
            factorial = factorial*i
            i=i+1
    return (factorial)

def abs(num):
    if num<0:
        num=(-1)*num
        return (num)
    else:
        return (num)

def exponent(num):
    i=100
    exp=0
    j=1
    while (i>0):
        exp=exp+(pow(num,j))/(factorialFun(j))
        j=j+1
        i=i-1
    return (1+exp)

def Ln(num):
    if num<=0:
        return (0)
    else:
        yNext=0
        y=num-1.0
        while (abs(y-yNext)>0.001):
            y=yNext
            yNext=y+2*((num-exponent(y))/(num+exponent(y)))
        return (yNext)


def XtimesY(x,y):
    if x>0:
        return (exponent(y*Ln(x)))
    else:
        return (0)

def sqrt(x,y):
    if x%2.0==0.0:
        if y<0.0:
            return (0)
    return(XtimesY(y, 1.0/x))

def calculate(x):
    if x==0:
        return (0)
    elif x%2.0==0.0:
        if x<0.0:
            return (0)
    return(exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x))

def calculate(x:float) -> float: