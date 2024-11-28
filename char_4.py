'''4. Write a program to find whether a given username contains less than 10 
 characters or not.'''

name=input(("enter name: "))
# char=name.len(name)  -->dont put name agian argument
char = len(name)
if(char<=10):
 print(f"WELCOME {name}")
else:
 print("Your name is too long.")

#  KEY FEATURE KNOWLWDGE--->  THE issue in this  code was in the way the len() function is applied. The len() function should be used directly on the variable without passing it again as an argument. Here is the corrected version of your code

