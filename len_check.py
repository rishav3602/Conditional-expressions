"""
Write a program to check if the given username contain less than 10 characters or not.
"""

username = input("Enter your username : ")
if len(username) < 10:
    print(f"It has less than 10 characters")
else:
    print(f"It has more than 10 characters")