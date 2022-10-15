"""
Write a program to check weather a student is pass or fail.
It requires total 40% and 33% in each subject to pass.
Assume 3 subjects and take marks entered by the user.
"""

sub1 = int(input("Enter the makrs of the subject 1 : "))
sub2 = int(input("Enter the makrs of the subject 2 : "))
sub3 = int(input("Enter the makrs of the subject 3 : "))
if (sub1+sub2+sub3)/3 >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33 :
    print(f"You have successfully passed the examination")
else:
    print(f"You are fail")