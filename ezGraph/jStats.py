def myAvg(lst):
    s = 0 
    n = 0 
    for i in lst: 
        s = s + i #sum
        n += 1 #number of numbers
    return s / n 

#residuals 
def residual (lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(len(lst1)):
        d = (lst1[i] - lst2[i]) **2
        s += d
        #print(i, lst1[i], lst2[i], d, s)
    return s 

#r = residual (y_measured, y_modeled)
#print (f'residual = {r}')

#difference from the mean 
def dsq (lst):
    n = len(lst)
    s = 0
    for i in range(n):
        d = (lst[i] - myAvg(lst)) **2
        s += d 
    return s 

#Rs value 
def rSquared (lst1, lst2):
    r2 = 1 - (residual (lst1, lst2)/ dsq(lst1))
    return r2

