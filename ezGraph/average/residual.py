y_measured = [0, 10, 20, 30, 40, 50]
def avg1 (lst):
    return sum (lst)/ len (lst)

def myAvg(lst):
    s = 0 
    n = 0 
    for i in lst: 
        s = s + i 
        n += i
        return s / n 

#residuals 
def residual (lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(len(lst1)):
        d = lst1[i] - lst2[i] 
        s += d
        #print(i, lst1[i], lst2[i], d, s)
    return s 


x1 = [2, 5, 7]
x2 = [3, 1, 1]

r = residual (x1, x2)
print (f'residual = {r}')

