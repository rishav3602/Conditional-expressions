"""
Write a program to check the grade of a student from his marks from his marks by following scheme.
  90-100 = EX
  80-90 = A
  70-80 = B
  60-70 = C
  50-60 = D
  40-50 = E
  40 < Fail
"""



from doctest import FAIL_FAST


marks = int(input("Enter your marks : "))
if 90 <= marks <= 100:
    grade = "EX"
elif 80 <= marks <= 90:
    grade = "A" 
elif 70 <= marks <= 80:
    grade = "B" 
elif 60 <= marks <= 70:
    grade = "C"
elif 50 <= marks <= 60:
    grade = "D"
elif 40 <= marks <= 50:
    grade = "E" 
else:
    grade = "FAIL"
print(f"The grade you obtained in the exam is : {grade}")