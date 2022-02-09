import random




def green_background(str):
  return "\33[7;49;32m " + str + " \33[0;49;37m"

def gray_background(str):
  return "\33[7;49;90m " + str + " \33[0;49;37m"

def yellow_background(str):
  return "\33[7;49;93m " + str + " \33[0;49;37m"





def load_words():
  with open('/usr/share/dict/words') as infile:
    word_list = infile.read().splitlines()
  return word_list

old_word_list = load_words()

word_list = []

count = 0

for word in old_word_list:
  count += 1
  print("Filtering word", count, "of", len(old_word_list))
  if len(word) == 5:
    word_list.append(word.upper())

print("\n\nLoaded!\n\n")





secret_word = random.choice(word_list)

print(secret_word)


print("""_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _


""")

while 1:
  guess = input("Try to guess the 5-letter word: ").upper()

  colored_guess = []

  if guess == "":
    print("Please type something!")
  elif guess not in word_list and len(guess) == 5:
    print("That's not a known word!")
  elif len(guess) != 5:
    print("Please guess a 5-letter word only!")
  else:
    guess_iterated = []
    for letter in guess:
      if secret_word[len(guess_iterated)] == letter:
        print(letter, "IS in", secret_word, "AND IT IS GREEN")
        colored_guess.append(green_background(letter))
      elif letter in secret_word and guess_iterated.count(letter) < secret_word.count(letter):
        colored_guess.append(yellow_background(letter))
      else:
        colored_guess.append(gray_background(letter))
        print(letter, "is NOT in", secret_word)
      guess_iterated.append(letter)

  colored_guess = "".join(colored_guess)

  print(colored_guess)


# list_of_words = []
# for word in old_word_list:
#   print(word)
#   print(len(word))
#   if len(word) == 5:
#     list_of_words.append(word)

# print(list_of_words)
# print(len(list_of_words))