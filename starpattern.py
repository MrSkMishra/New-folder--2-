###################################################################### Normal Star Patern ################################################
# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()


##################################################################### Increasing Triangle Pattern #######################################


# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

################################################################# decreasing Triangle Pattern ##################################################


# we just only add end in second for loop (i,n)

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="")
#     print()


############################################################### right sided triangle ###############################################

#      *
#     **
#    ***
#   ****
#  *****

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()



#           *
#         **
#       ***
#     ****
#   *****

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for k in range(i+1):
#         print("*",end="")
#     print()


############################################## Hill Triangle Pattern #################################################################

#      * 
#     * * 
#    * * *
#   * * * *
#  * * * * *

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()




#      *
#     ***
#    *****
#   *******
#  *********


############################################## Reverse Hill Triangle Pattern #################################################################

# *********
#  *******
#   *****
#    ***
#     *


# n = 5
# for row in range(n):                   
#    for j in range(row):
#       print(" ",end="")
#    for j in range(2*(n-row)-1):
#       print('*',end="")
#    print()

      


############################################################ Right sided triangle in reverse order #####################################

#   * * * * * 
#     * * * * 
#       * * *
#         * *
#           *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()


######################################################################### Diamond Patterns ######################################################################################

# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i+1-1):
#         print("*",end= " ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()





#    * 
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *



# n = 4
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n-1):
#         print("*",end="")
#     for l in range(i,n):
#         print("*",end="")
#     print()




#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *



################################################### Square Star Pattern #############################################################

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

################################################## Hollow Square Star Pattern ##########################################################

# n = 4  # taking only one input
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n = 4 # taking two input
# m = 4
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if i==1 or i==n or j==1 or j==m:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


########################################################### Rhombus Star Pattern #########################################################

# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(1,n+1):
#         print("*",end="")
#     print()



#  ****
#   ****
#    ****
#     ****


######################################################### Rectangle Star Pattern ####################################################

# n = 4
# for i in range(n):
#     for j in range(n+1):
#         print("*",end="")
#     print()

####################################################### Hollow Rectangle Star Pattern #####################################################

# n = 4
# m = 6
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if i==1 or i==n or j==1 or j==m :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
##################################################### Parallelogram Star Pattern ########################################################

# n = 4
# m = 6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for k in range(1,m+1):
#         print("*",end="")
#     print()


#################################################### Mirrored Rhombus Star Pattern #####################################################

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(n):
#         print("*",end="")
#     print()

################################################## Triangle Star Pattern ##################################################################

# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

################################################ Pyramid Star Pattern ##############################################################

# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


#     * 
#    * * 
#   * * *
#  * * * *
   

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         print("*",end="")
#     print()


#    *
#   ***
#  *****
# *******

############################################ Hollow Pyramid Star Pattern ###########################################################


# n = 4
# for  i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i+1):
#         if k == 0 or k == 2*i or i == n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#     *
#    * *
#   *   *
#  *******


#################################### Inverted Pyramid Star Pattern ###############################################################################

# n = 4
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*(n-i)-1):
#         print("*",end="")
#     print()

# *******
#  *****
#   ***
#    *

#####################################  Inverted Hollow Pyramid Star Pattern #################################################################

# n = 4
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         if i == 0 or i == n or k == 2*i-2 or k == 0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# *******
#  *   *
#   * *
#    *


##################################### Half Diamond Star Pattern ####################################################################

# n = 4
# for i in range(n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
# for k in range(1,n):
#     for l in range(k,n):
#         print("*",end="")
#     print()
 
###################################### Half Diamond Star Pattern Inverted ################################################################

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print("*",end="")
#     print()


###################################### Diamond Star Pattern ###########################################################################

# above and below Both Are Same Difference is just a space between second for loop of every nested at (end=" ")

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print("*",end=" ")
#     print()

############################################## square number pattern #######################################################################

# n  = 4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

############################################ Left Triangle number Pattern #########################################################

# n = 4
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

################################################################# decreasing Triangle number Pattern ##################################################

# we just only add end in second for loop (i,n)

# n = 5
# for i in range(1,n):
#     for j in range(i,n):
#         print(j,end="")
#     print()

############################################################### right sided triangle ###############################################



# n = 5
# for i in range(n+1):
#     for j in range(i,n+1):
#         print(' ',end=" ")
#     for k in range(i+1):
#         print(k,end=" ")
#     print()

######################################################################################################################################

#           *
#         **
#       ***
#     ****
#   *****

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for k in range(i+1):
#         print(k,end="")
#     print()

######################################### alphabets pattern #############################################################################

## A-Z = [65-90]
## a-z = [97-122]
## 0-9 = [48-57]

# n = 4
# alphabet = 65
# for i in range(n+1):
#     for j in range(i+1):
#         print(chr(alphabet),end=" ")
#     alphabet += 1
#     print()

# A 
# B B 
# C C C
# D D D D
# E E E E E
#########################################################################################################################################

print()

# n = 4
# alphabet = 65
# for i in range(n+1):
#     for j in range(i,n+1):
#         print(chr(alphabet),end=" ")
#     alphabet = alphabet+1
#     print()

# A A A A A 
# B B B B
# C C C
# D D
# E
###############################################################################################################################################

# n = 4
# alphabet = 65
# for i in range(n+1):
#     for j in range(i,n+1):
#         print(chr(alphabet),end=" ")
#     alphabet = alphabet+2
#     print()

# A A A A A 
# C C C C
# E E E
# G G
# I

##########################################################################################################################################

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#              print("A",end=" ")
#         else:
#             print("B",end=" ")
#     print()

# A
# B B
# A A A
# B B B B
# A A A A A

##################################################################################################################################################




# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n):
#         if i%2== 0:
#             print("Z",end="")
#         else:
#             print("O",end="")
#     print()

#  ZZZZZ
#   OOOO
#    ZZZ
#     OO
#      Z

######################################################################################################################################


# n = 4
# alphabets = 65
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(chr(alphabets),end=" ")
#     alphabets = alphabets+1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print(chr(alphabets),end=" ")
#     alphabets = alphabets+1
#     print()


#    A
#   B B
#  C C C
# D D D D
#  E E E
#   F F
#    G



######################################################################################################################################



# n = 5
# alphabets = 65
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(chr(alphabets),end=" ")
#     alphabets = alphabets+1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print(chr(alphabets),end=" ")
#     alphabets -= 1
#     print()

#     A 
#    B B
#   C C C
#  D D D D
# E E E E E
#  F F F F 
#   E E E 
#    D D
#     C


##################################################################################################################################


# n = 5  # change this to adjust the size of the pattern

# # upper part of the diamond
# for i in range(n):
#     spaces = " " * (n-i-1)
#     letters = chr(65+i) + " " * i * 2 + chr(65+i)
#     print(spaces + letters)

# # lower part of the diamond
# for i in range(n-1, -1, -1):
#     spaces = " " * (n-i-1)
#     letters = chr(65+i) + " " * i * 2 + chr(65+i)
#     print(spaces + letters)

#     AA
#    B  B
#   C    C
#  D      D
# E        E
# E        E
#  D      D
#   C    C
#    B  B
#     AA
    
####################################################################################################################################


# n = 5
# alphabet = 65
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i):
#         print(chr(alphabet),end="")
#     for l in range(i+1):
#         print(chr(alphabet),end="")
#     alphabet += 1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n-1):
#         print(chr(alphabet),end="")
#     for l in range(i,n):
#         print(chr(alphabet),end="")
#     alphabet = alphabet-1
#     print()


#      A
#     BBB
#    CCCCC
#   DDDDDDD
#  EEEEEEEEE
#   DDDDDDD
#    CCCCC
#     BBB
#      A

#########################################################################################################################################


# n = 4
# for i in range(n):
#     alphabet = 65   
#     for j in range(i+1):
#         print(chr(alphabet),end=" ")
#         alphabet = alphabet + 1
#     print()

# A 
# A B 
# A B C 
# A B C D 


######################################################################################################################################


# n = 5
# for i in range(n):
#     alphabets = 65
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i,n):
#         print(chr(alphabets),end="")
#         alphabets += 1
#     print()

# ABCDE
#  ABCD
#   ABC
#    AB
#     A

#####################################################################################################################################

# n = 5
# for i in range(n):
#     alphabets = 65
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i):
#         print(chr(alphabets),end="")
#         alphabets = alphabets+1
#     for l in range(i+1):
#         print(chr(alphabets),end="")
#         alphabets = alphabets+1
#     print()


#      A
#     ABC
#    ABCDE
#   ABCDEFG
#  ABCDEFGHI



# n = 5
# for i in range(n):
#     alphabets = 65
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(chr(alphabets),end=" ")
#         alphabets = alphabets+1
#     print()

#     A
#    A B
#   A B C
#  A B C D 
# A B C D E

######################################################################################################################################

# n = 5
# for i in range(n):
#     alphabets = 69
#     for j in range(i+1):
#         print(chr(alphabets),end="")
#         alphabets = alphabets-1
#     print()

# E
# ED
# EDC
# EDCB
# EDCBA

########################################################################################################################################

# n = 5
# alpha = 69
# for i in range(n):
#     alphabets = alpha
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n):
#         print(chr(alphabets),end="")
#         alphabets = alphabets+1
#     alpha = alpha - 1
#     print()

#  EFGHI
#   DEFG
#    CDE
#     BC
#      A

########################################################################################################################################

# n = 5
# for i in range(n):
#     alphabets = 65
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(chr(alphabets),end=" ")
#         alphabets = alphabets + 1
#     print()

#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 

######################################################################################################################################


# n = 5 
# for i in range(n):
#     alphabets = 65
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i):
#         print(chr(alphabets),end="")
#         alphabets = alphabets + 1
#     for l in range(i+1):
#         print(chr(alphabets),end="")
#         alphabets = alphabets-1
#     print()


#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA


#############################################################################################################################################


# string = 'CODER'
# n = len(string)
# p = 0
# for i in range(n):
#     for j in range(i+1):
#         print(string[p],end="")
#     p = p+1
#     print()

# C
# OO
# DDD
# EEEE
# RRRRR


########################################################################################################################################

# string = 'CODER'
# n = len(string)
# p = n-1
# for i in range(n):
#     for j in range(i+1):
#         print(string[p],end="")
#     p = p-1
#     print()


# R
# EE
# DDD
# OOOO
# CCCCC


##########################################################################################################################################

# string = "CODER"
# n = len(string)
# for i in range(n):
#     p = 0
#     for j in range(i+1):
#         print(string[p],end="")
#         p = p+1
#     print()

# C
# CO
# COD
# CODE
# CODER


############################################################################################################################################

# string = 'CODER'
# n = len(string)
# for i in range(n):
#     p = n-1
#     for j in range(i+1):
#         print(string[p],end="")
#         p = p-1
#     print()

# R
# RE
# RED
# REDO
# REDOC


####################################################################################################################################

# string = "CODER"
# n = len(string)
# k = n-1
# for i in range(n):
#     p = k
#     for j in range(i):
#         print(" ",end="")
#     for k in range(i,n):
#         print(string[p],end="")
#         p = p-1
#     print()
#     k = k-1