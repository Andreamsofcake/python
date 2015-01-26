# # excercise 1
# color = input("What is your favorite color? ")
# if color == "brown":
#   print("{} is POOOP".format(color))
# else:
#   print("You look good in {}".format(color))
# # excercise 2
# number_1 = input("First number ")
# number_2 = input("Second number ")
# number_3 = input("Third number ")
# max_of_three = max(number_1, number_2,  number_3)
# print (max_of_three)
# # # excercise 3
# name = input("What is your name?")
# print(name.count(""))
# # excercise 4
# letter = input("Enter a letter ")
# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#   print("vowel")
# else:
#   print("consonent")
# # excercise 5
user_word = input("What is your word? ")
user_num = input("What is the ratio? ")

try:
  num = int(user_num)
except:
  num = float(user_num)

if not "." in user_num:
  print(user_word[num])
else:
  ratio = round(len(user_word)*num)
  print(user_word[ratio])