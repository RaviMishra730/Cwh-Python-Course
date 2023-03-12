text = input("Enter the text\n")

if ("Make Money online by buying the products" in text):
    spam = True
elif("buy now and you will get cashback of 1 crore" in text):
    spam = True
elif("Click This!" in text):
    spam = True
elif("subscribe this " in text):
    spam = True
else:
    spam = False


if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

# text = input("Enter the text\n")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")