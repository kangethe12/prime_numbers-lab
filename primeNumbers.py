
def primeNumbers(number):
 list_of_prime_num = []

 for i in range(2, number): # loops through 2 3 4 5 6 7
   prime = True

   for x in range(2, i): # 2,3
     if i % x == 0: 
       prime = False

   if prime == True:
     list_of_prime_num.append(i)

 return list_of_prime_num

print (primeNumbers(20))