"""
Write a program to check if the given name is present in the list or not.
"""
list = ["Gaurav","Rishav","Ujjwal","Mayank","Rohit"]
name = input("Enter the name you want to check : ")
if name in list:
    print(f"{name} is present in the given list.")
else:
    print(f"{name} is not present in the given list.")