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
# user_word = input("What is your word? ")
# user_num = input("What is the ratio? ")

# try:
#   num = int(user_num)
# except:
#   num = float(user_num)

# if not "." in user_num:
#   print(user_word[num])
# else:
#   ratio = round(len(user_word)*num)
#   print(user_word[ratio])
# # excercise 6
# 
# full_name = "Andrea Moulding"
# name_list = full_name.split(" ")
# greeting_list = "Hi, I'm {}".format(name_list[0]).split(" ")
# greeting = " ".join(greeting_list)
# print(greeting)
# # excercise 7
# book_list = []

# def show_help():
#   print("\nSeparate each item with a comma.")
#   print("Name of the Book?")
#   print("Enter HELP for instructions")
#   print("Enter SHOW to show list")
#   print("Enter DONE to stop")

# def add_to_list(books):
#   book_list.append(books)
#   print("Added {} to list".format(books))

# def show_books():
#   print("Here are your books:")
#   count = 1
#   for books in book_list:
#     print("{}: {}".format(count, books))
#     count += 1

# show_help()

# while True:
#   new_book = input("> ")
#   if new_book == "DONE":
#     show_books()
#     break
#   elif new_book == "HELP":
#     show_help()
#     continue
#   elif new_book == "SHOW":
#     show_books()
#     continue
#   add_to_list(new_book)
#   continue
# #   excercise 8

# new_list = [1, 2, 3, 4]

# def add_list(list):
#   amount = 0
#   for num in list:
#     amount += num
#   return amount

# print(add_list(new_list))
# # exercise 9
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = list_1 + list_2
# print(list_3)
#
# # exercise 10
# my_list = ["One", "Two", "Three", "Four"]
# vowels = list("aeiou")
# response = []

# for numbers in my_list:
#   numbers_list = list(numbers.lower())

#   for vowel in vowels:
#     while True:
#       try:
#         numbers_list.remove(vowel)
#       except:
#         break
#   response.append(''.join(numbers_list).capitalize())

# print(response)
#

# names = ['Ken', 'Sam', 'Bob']

# names_1 = names.pop()

# print(names_1)
#
# exercies 12
book_list = []
def move_item(idx, new_idx):
  index = idx - 1
  new_index = new_idx - 1
  item = book_list.pop(index)
  book_list.insert(new_index, item)

def remove_item(idx):
  index = idx - 1
  item = book_list.pop(index)
  print("Removed {}".format(item))

def show_help():
  print("Name of the Book?")
  print("Enter HELP for instructions")
  print("Enter SHOW to show list")
  print("Enter DONE to stop")
  print("Enter REMOVE to remove book")
  print("Enter MOVE to move to new number")

def add_to_list(books):
  book_list.append(books)
  print("Added {} to list".format(books))

def show_books():
  print("Here are your books:")
  count = 1
  for books in book_list:
    print("{}: {}".format(count, books))
    count += 1

show_help()

while True:
  new_book = input("> ")
  if new_book == "DONE":
    show_books()
    break
  elif new_book == "HELP":
    show_help()
    continue
  elif new_book == "SHOW":
    show_books()
    continue
  elif new_book =="REMOVE":
    show_books()
    idx = input("Book number?")
    remove_item(int(idx))
    continue
  elif new_book =="MOVE":
    show_books()
    idx = input("Book number?")
    new_idx = input("New book number?")
    move_item(int(idx), int(new_idx))
    show_books()
    continue
  add_to_list(new_book)
  continue
