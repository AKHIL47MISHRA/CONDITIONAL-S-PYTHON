# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

a='''  "Make a lot of money",   "buy now" ,  "subscribe this" ,  "click this"
'''
comment=input("enter your cmt: ").lower()
is_spam = any(keyword in comment for keyword in a)

if is_spam:
    print("spammers fuck you: ")
else:
    print("good comment LOVE YOU: ")


                #   EXPLAINANTION

'''         The any() function is used here. It checks if any of the keywords in the A list are present in the comment.

The for keyword in A part iterates through each keyword in the spam_keywords list.

keyword in comment checks if the current keyword is a substring of the comment.

If any keyword is found in the comment, any() returns True, meaning the comment is spam. If none of the keywords are found, it returns False.

'''

# spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# comment = input("Enter your comment: ").lower()

# is_spam = any(keyword in comment for keyword in spam_keywords)

# if is_spam:
#     print("Spam detected: Please avoid using spammy phrases.")
# else:
#     print("Good comment: Thank you for your input!")
