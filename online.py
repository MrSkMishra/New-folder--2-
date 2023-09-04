# n = 4               
# for i in range(n-1):  
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i*2+1):
#             print("*",end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i*2,n*2-1):
#         print("*",end="")
#     print()

# 1. a single string of star and space is not accepted
# ex: "*<space>" and "<space>*" these are not accepted

# 2. Do not hard code spaces.

# 3. Try to find a logic for printing the spaces.

# If you are coding in python : 
# 4. end="<space>" this is also not accepted




'''
 *
* *
'''


# n = 50
# if n == 20:
#     print("*",end="")
# else:
#     for i in range(1,n+1):

#         for j in range(1,n-i+1):
#                 print(" ",end="")
#         for k in range(1,i+1):
#             print("*",end="")
#             if j != i  or i == 2 or i == 25:
#                 print(" ",end="")
#         print()
        # or i == i*10

# n = 30
# max_length = 80
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     stars = "* "*i
#     if len(stars)>max_length:
#         numlines = len(stars)
#         for k in range(numlines):
#             line = stars[k*max_length : (k+1)*max_length].strip()
#             print(line)
#     else:
#         print(stars.strip())