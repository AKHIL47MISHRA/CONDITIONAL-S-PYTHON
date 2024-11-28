'''6. Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F
'''
marks=int(input("Enter your marks: "))
if(marks>=90 and marks<=100):
    print("HURRAH 😎 you hit the grade A")
elif(marks>=80 and marks<=90):
    print("🫵 ohh you hit the grade B")
elif(marks>=70 and marks<=80):
    print("enjoy you hit the grade C")
elif(marks>=60 and marks<=70):
    print("welldone you hit the grade D")
# elif(marks<=50):
#     print("AFSHOSH FUKKA lag gaya")
else:
    print("AFSHOSH FUKKA lag gaya")
