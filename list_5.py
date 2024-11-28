'''5. Write a program which finds out whether a given name is present in a list or not.'''



names_list=["akhil" , "monu" , "abhi" , "sunny"]
entered_name=(input("enter your  name: "))
# is_avl= any(keyword in list for keyword in a)
if entered_name in names_list:
# if is_avl:
    print("you are alredy avaiable in list")
else:
    print("welcome you are new in list ")
                      
'''YOU can learn from this code we dont want to use any() keyword with strring value wee will dirrectly put the stat--->if entered_name in names_list it will search automaty and work corretly '''