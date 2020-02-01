
def Fibonacci (n): 
   if n <= 1:  
      return n  
   else:
      return(Fibonacci (n-1) + Fibonacci (n-2))
   
# ---take input from the user---  
Fib = int(input("[+] How many Numbers of Fibonacci you wont to Print : "))  
# ---check the number is valid---
if Fib <= 0:  
   print("----[-Plese enter a positive integer Fibonacci have no Nagetive function-]---")  
else:  
   print("[=] Fibonacci sequence is following :")  
   for i in range(Fib):  
       print(Fibonacci (i))
       
       
