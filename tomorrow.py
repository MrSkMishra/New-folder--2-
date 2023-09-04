# n = 4
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         if k == 0 or k == i*2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i*2,n*2-1):
#         if k == i*2 or k == n*2-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


n = 4
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k == 0 or k == i*2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(i*2,n*2-1):
        if k == i*2 or k == n*2-2:
            print("*",end="")
        else:

            print(" ",end="")
    print()

# if True == 1:
#     print("Boolean")

# if False == 0:
#     print("jeggeububer")




# def pattern(n):
#     for i in range(1,n+1):
#         for j  in range(1,2*n):
#             if i >(n-j+1):
#                 print("",end=" ")
#             else:
#                 print("*",end="")
#             if i + n - 1 > j:
#                 print("",end=" ")
#             else:
#                 print("*",end="")
#         print("")
#     for i in range(1,n+1):
#         for j in range(1,2*n):
#             if i < j:
#                 print("",end=" ")
#             else:
#                 print("*",end="")
#             if i < 2*n-j:
#                 print("",end=" ")
#             else:
#                 print("*",end="")
#         print("")
            


# pattern(5)





# n = -5
# if n > 0:
#     print("positive")
# else:
#     print("negative")

# n = 21
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")



# n = 5
# sum_1 = 0
# for i in range(1,n+1):
#     sum_1 = sum_1 + i
# print(sum_1)



# n = 5
# m = 2
# if n > m:
#     print("n is greater than m")
# else:
#     print("m is greater than n")

# n = 5
# if n % 4 == 0:
#     print("it's a leap year")
# else:
#     print("it's not a leap year")


# n = 7
# flag = 0
# if n == 0 or n == 1:
#     print("not a prime number")

# else:
#     for i in range(2,n):
#         if n%i == 0:
#             flag = 1
#             break
#     if flag == 1:
#         print("not prime")
#     else:
#         print("prime")


################################################### lambda function #########################################################

# x = lambda x:x**2
# answer = x(2)
# print(answer)



# n = 15
# for i in range(1,n):
#     flag = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             flag += 1
#     if flag == 2:
#         print(i,end=" ")



# def swap(pos1,pos2):
#     l[pos1],l[pos2] = l[pos2],l[pos1]
#     return print(l)

# l = [23,4,4,5,6666,6,6]
# swap(2,4)


# string = "prepinsta"
# l = ['A','E','I','O','U','a','e','i','o','u']
# print("After removing vowels : ",end="")

# for i in string:
#     if i not in l:
#         print(i,end="")


# l = [1,2,3,54,5565]
# l_1 = []
# for i in enumerate(l):
#     l_1.append(i)
# print(l_1)

# n = 99
# sqr = ""
# for i in str(n):
#     mul = int(i)*int(i)
#     sqr = str(sqr)+str(mul)
# print(sqr)



                
                
# m = 15
# n = 30
# for i in range(n, m-1, -1): #(start,stop,step))
#     if i < 2:
#         continue
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False    
#             break
#     if is_prime: 
#         print(i,"hye",end=" ")
# print()


# n =15
# m = 30
# for i in range(m,n-1,-1):
#     if i < 2:
#         continue
#     flag = True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             flag = False
#             break
#     if flag:
#         print(i,end=" ")

# n = 355
# sum_n = 0
# for i in str(n):
#     sum_n = int(i) + int(sum_n)
# print(sum_n)

# n = 9
# sum_n = 0
# for i in range(1,n+1):
#     sum_n = i+sum_n
# print(sum_n)

# n = 56656
# rev = ""
# for i in str(n):
#     rev = i+rev
# print(rev)

# n = 121
# rev = ""
# for i in str(n):
#     rev = i + rev
# if n == int(rev):
#     print("palindrome")
# else:
#     print("not palindrome")

# n = 153
# temp = n
# sum_n = 0
# digits = len(str(n))
# while temp != 0:
#     rem = temp%10
#     sum_n = rem**digits+sum_n
#     temp = temp//10
# if sum_n == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# n = 10
# n1 = 0
# n2 = 1
# print("Fibonacci series :- ",n1,n2,end=" ")
# for i in range(2,n+1):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")

# n = 10
# n1 = 0
# n2 = 1
# print("Fibonacci series :- ")
# for i in range(2,n+1):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
# print(n3,end=" ")


# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact,end=" ")

# n = 3
# power = 4
# output = 1
# for i  in range(1,power+1):
#     output = n*output
# print(output)

# n = 10
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i,end=" ")

# n = 21
# l = []
# def prime_factor(n):
#     if n < 4:
#         return n
#     while n > 1:
#         for i in range(2,n//2+2):
#             if i == n//2+1:
#                 l.append(n)
#                 n = n//n
#             if n%i == 0:
#                 l.append(i)
#                 n = n//i
#                 break
#     return print(l) 
# prime_factor(n)
    

# n = 145
# sum = 0
# temp = n
# while n:
#     i = 1
#     fact = 1
#     rem = n%10
#     while i <= rem:
#         fact = fact*i
#         i = i +1
#     sum = sum +fact
#     n = n//10
# if temp == sum:
#     print("Strong")
# else:
#     print("not strong")




# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# import urllib.error
# import time
# from multiprocessing import Pool
# from requests.exceptions import HTTPError

# start = time.time()

# file = open('users.txt', 'r', encoding="ISO-8859-1")
# urls = file.readlines()
# for url in urls:
#     url = url.strip ('\n')
#     try:
#         req = requests.get(url)
#         req.raise_for_status()
#     except HTTPError as http_err:
#         output = open('output2.txt', 'a')
#         output.write(f'не найдена\n')  
#     except Exception as err:
#         output = open('output2.txt', 'a')
#         output.write(f'не найдены\n')  
#     else:
#         output = open('output2.txt', 'a')
#         soup = BeautifulSoup(req.text, "lxml")
#         the_url = soup.select("[rel='canonical']")[0]['href']
#         the_url2=the_url.replace('https://www.instagram.com/','')
#         head, sep, tail = the_url2.partition('/')
#         output.write (head+'\n')




