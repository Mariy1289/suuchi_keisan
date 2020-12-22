def f (x):
    return x**3 - 2*x


xl = 1 
xr = 2

count=0

for _ in range (10):
    mid = ( xr + xl ) /2 
    if ( f(mid) > 0 and f(xr) > 0 ) or (f(mid) < 0 and f(xr) < 0): 
        xr = mid 
    else : xl = mid 
    count+=1

    print ("step",count,":", mid, f(mid))