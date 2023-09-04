"""Write a function named capital indexes. The function takes a single parameter,which is a string. Your function should return a list of all the indexes in the
string that have capital letters. For example, calling capital indexes(”HeLlO”) should return the list [0, 2, 4]"""

# def capital_indexes(n):
#     # return print([n[i] for i in range(len(n)) if n[i].isupper()])  #['H', 'L', 'O']
#     # return print([n for i in range(len(n)) if n[i].isupper()])  #['HeLlO', 'HeLlO', 'HeLlO']
#     return print([i for i in range(len(n)) if n[i].isupper()])  # [0, 2, 4]


# n = "HeLlO"
# capital_indexes(n)


# l = [1,2,3,4,5]
# name = []
# name = l[2:]

# rev = ""
# print(name)
# for i in str(name):
#     rev = i+rev
# print(rev)



# n = 5
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i*2+1):
#         if k == 0 or k == i *2:
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





# import datetime

# def find_day_of_birth():
#     # Get the user's input for the date of birth
#     dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

#     try:
#         # Convert the user's input into a datetime object
#         dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d")

#         # Get the day of the week for the date of birth
#         day_of_birth = dob.strftime("%A")

#         # Print the result
#         print("You were born on a", day_of_birth)
#     except ValueError:
#         print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

# # Call the function to find the day of birth
# find_day_of_birth()