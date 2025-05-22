
import math

print("1:Square root")
print("2:Square")
print("3:Log")
print("4:Factorial")
print("5:Addition")
print("6:Difference")
print("7:Product")
print("8:Divide")


a  = int(input("Enter number: "))



if(a  == 1):
    num = int(input("Enter number: "))
    c  = math.sqrt(a)
    print("Squre root is ",c)
 
 

if(a == 2):
    d = int(input("Enter a num: "))
    e = d*d
    print("secqura is ",e)
    
    
if(a == 3): 
    f = int(input("Enter num: "))
    g = (math.log(f))
    print("log is ",g)    
    
    
if(a == 4):
    h = int(input("Enter num: "))
    i = (math.factorial(h))
    print("Factroial is ",i)    
    
    
if(a == 5):
    j = int(input("Enter first num: "))
    k = int(input("Enter second num: "))
    l  = j + k
    print("Sum is ",l)
    
    
if(a == 6):
    m = int(input("Enter first num: "))
    n = int(input("Enter second num: "))
    o = m - n
    print("Difference is ",o)
    
    
if(a == 7):
    p = int(input("Enter first num: "))
    q = int(input("Enter second num: "))
    r = p * q
    print("Product is ",r)   
    
    
if(a == 8):
    s = int(input("Enter first num: "))
    t = int(input("Enter second num: "))
    u = s / t
    print("Division is ",u)    
    
    
