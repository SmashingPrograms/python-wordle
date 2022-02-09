def load_words():
  with open('/usr/share/dict/words') as infile:
    word_list = infile.read().splitlines()
  return word_list

old_word_list = load_words()

word_list = []

count = 0

for word in old_word_list:
  count += 1
  print("Loading word ", count, " of ", len(old_word_list))
  if len(word) == 5:
    word_list.append(word.upper())

print("\n\nLoaded!\n\n")





def green_background(str):
  return "\33[7;49;32m" + str + "\33[0;49;37m"

def gray_background(str):
  return "\33[7;49;90m" + str + "\33[0;49;37m"

def yellow_background(str):
  return "\33[7;49;93m" + str + "\33[0;49;37m"


# list_of_words = []
# for word in old_word_list:
#   print(word)
#   print(len(word))
#   if len(word) == 5:
#     list_of_words.append(word)

# print(list_of_words)
# print(len(list_of_words))