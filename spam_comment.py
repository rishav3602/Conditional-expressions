"""
A spam comment is defined as the sentence containing the following keywords.
{"make a lot of money","buy now","subscribe this","click this"}
Write a program to detect these spams.
"""

text = input("Enter your text : ")
spam = False
if ( "make a lot of money"  in text ):
    spam = True
elif ( "buy now" in text ) :
    spam = True    
elif (  "subscribe this"  in text ) :
    spam = True    
elif ( "click this" in text ) :
    spam = True    
else:
    spam = False
if spam is True :
    print(f"The given text is a spam")
else:
    print(f"The given text is not a spam")
