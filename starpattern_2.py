import time
################################################################ right sided triangle ##############################################
# n = 5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()

#      *
#     **
#    ***
#   ****
#  *****



######################################################## Normal Star Patern #####################################################

# n = 4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="")
#     print()

############################################ list iteration ####################################################################

# l =[1,4,5,6,7,7,8,8,8,8,7,66,6,6,6,"j"]

# for i in l:
#     print(i)
    
############################################### Palindrome Of a list ############################################################    

# start_time = time.time()
# my_list = ["racecar", "hello", "world", "level", "python"]

# for item in my_list:
#     if item == item[::-1]:
#         print(item, "is a palindrome")
# print("--- %s seconds ---" % (time.time() - start_time))


################################### diamond pattern with two for loops ############################################

# n = 5
# for i in range(n):
#     alpha = 65
#     print(" " * (n-i-1) + chr(alpha) * (2*i+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1) + chr(alpha) * (2*i+1))
#     alpha+=1


############################################################ Right sided triangle in reverse order #####################################

# n = 4
# for i in range(1,n+1):
#     alpha = 65
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print(chr(alpha),end="")
#         else:
#             print(" ",end="")
#         alpha = alpha+1
#     print()

# ABCD
# A  D
# A  D
# ABCD




# n=4
# alpha = 65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for k in range(1,n+1):
#         if j % i == 0:
#             print(chr(alpha),end="")
#         alpha += 1
#     print()

#  ABCD
#   EFGH
#    IJKL
#     MNOP


# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")    
#     print()

# *
# **
# ***
# ****


################################################################## pattern #######################################################
# n = 4
# for i in range(n+1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n):
#         print("*",end="")
#     print()

#  ****
#   ***
#    **
#     *


#########################################Hollow Pyramid Star Pattern###########################################

############################################ Diamond Pattern ############################################################

# n = 4           
# for row in range(n-1):        #row = 0,1,2
#     for column in range(n-row-1):  # column = 4-0-1=3
#                                    # column = 4-1-1=2
#                                    # column = 4-2-1=1
#         print(" ",end="")          
#     for col1 in range(row*2+1):   # col1 = 0*2+1=1                     
#                                   # col1 = 1*2+1=3
#                                   # col1 = 2*2+1=5
        
#         print("*",end="")   #   *
#                             #  ***
#                             # *****
#     print()
# for row in range(n):            # 4                   
#     for column in range(row):   # row=0      
#                                 # row=1
#                                 # row=2
#                                 # row=3
#         print(' ',end="")
#     for col1 in range(row*2,n*2-1): #start : col1=0*2=0,stop : 4*2-1=7   
#                                     #start : col1=1*2=2, stop : 4*2-1=7
#                                     #start : col1=2*2=4, stop : 4*2-1=7
#                                     #start : col1=3*2=6, stop : 4*2-1=7
#         print('*',end="")        #*******        
#                                  # *****
#                                  #  ***
#                                  #   *
#     print()


######################################### working Example diamond ################################################################

# n=4
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         print("*",end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i*2,n*2-1):
#         print("*",end="")
#     print()

############################################### Explanation Of Diamond an odd number of rows #########################################


# n = 5
# while n % 2 == 0:   # 5%2!=0(True then execute)
#     n = int(input("Please enter an odd number of rows: "))
# for i in range(1, n+1, 2):   # Start : i = 1,3 Stop : 5+1, step : 2
#     for j in range((n-i)//2):# (5-1)//2=2
#                              # (5-3)//2=1
#                              # (5-5)//2=0
#         print(" ", end="")
#     for k in range(i):         # i=1
#                                # i=3
#                                # i=5
#         print("*", end="")
#     print()                     #  *
#                                 # ***
#                                 #*****
# for i in range(n-2, 0, -2):     # start: 5-2=3,1  stop : 0  step : -2
#     for j in range((n-i)//2):   # 5-3//2=1
#                                 # 5-1//2=2
#         print(" ", end="")
#     for k in range(i):          # i=3
#                                 # i=1
#         print("*", end="")     # *** 
#                                #  *
#     print()


##################################################### working example of Diamond an odd number of rows #########################################

# n=5
# for i in range(1, n+1, 2):
#     for j in range((n-i)//2):
#         print(" ",end="") 
#     for k in range(i):
#         print("*",end="")
#     print()
# for i in range(n-2, 0, -2):
#     for j in range((n-i)//2):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()


####################################### hollow Diamond Pattern ##################################################################

# n = 4
# for i in range(n-1):    # i = 0,1,2,3
#     for j in range(n-i-1):  # j = 4-0-1=3
#                             # j = 4-1-1=2
#                             # j = 4-2-1=1
#                             # j = 4-3-1=0
#         print(" ", end="")
#     for k in range(i*2+1):  #k = 0*2+1=1 k=0 ,1
#                             #k = 1*2+1=3 k=0,1,2
#                             #k = 2*2+1=5 k=0,1,2,3,4
#         if k == 0 or k == i*2:
#             print("*", end="")  #   *
#                                 #  * *
#                                 # *   *
                                    
#         else:
#             print(" ", end="")
#     print()
# for i in range(n):      # i=0,1,2,3
#     for j in range(i):  # j=0,1,2,3
#         print(" ", end="")
#     for k in range(i*2,n*2-1):  # start:-  k : 0*2=0    1,2,3,4,5,6  || stop :- 4*2-1=7
#                                 # start:-  k : 1*2=2    2,3,4,5,6  || stop :- 4*2-1=7
#                                 # start:-  k : 2*2=4    4,5,6  || stop :- 4*2-1=7
#                                 # start:-  k : 3*2=6    6  || stop :- 4*2-1=7
#         if k == i*2 or k == n*2-2:  #k == 4*2-2=6, 
#             print("*", end="")  #*     *
#                                 # *   *
#                                 #  * *
#                                 #   *
#         else:
#             print(" ", end="")
#     print()

########################################### pyramid pattern ################################################################

# n = 4
# for i in range(n+1):
#     for j in range(n-i+1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         if k == 0 or k == i*2 or i == n  :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

########################################### Inverted pyramid pattern ################################################################


# n = 4
# for i in range(n+1):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i*2,n*2-1):
#         if k == i*2 or k == n*2-2 or i == 0 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

    
        
###########################################################################################################################

# n = 5
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         if k==0 or k==i*2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*i,n*2-1):
#         if k==i*2 or k==n*2-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


############################################ hill hollow #########################################################

# n=4
# for i in range(n+1):
#     for j in range(n-i+1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         if k==0 or k==i*2 or i==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
        
################################################### Ulta star hill pattern #######################################################33

# n=4
# for i in range(n+1):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*i,2*n-1):
#         if k==i*2 or k==2*n-2 or i==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
