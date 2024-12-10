import numpy as np
import sys
sys.set_int_max_str_digits(10000000)
def fibonacci(n):
    a,b = 0,1

   
    liste = [a, b]

    for i in range(2,n):
        liste.append(liste[-1] + liste[-2])

    
    return np.array(liste)
   

print(fibonacci(100000))
