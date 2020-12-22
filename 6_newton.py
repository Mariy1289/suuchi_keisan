def f (x):
    return x**3 - 2*x

def fdash(x):
    return 3*(x**2) -2

x = 2
count=0

for _ in range (10):
    x = x - f(x)/fdash(x)
    count +=1
    print ("x", count, "= ", x ) 
    
