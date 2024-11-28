# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

s1=int(input("enter marks of s1: "))
s2=int(input("enter marks of s2: "))
s3=int(input("enter marks of s3: "))
result=((s1 + s2 + s3 ) / 300) * 100  
if(result < 40):
    print("you are failed with percenatge ", result)
elif(result >= 40):
    print("you are passed with percenatge ", result)

    # review this code 