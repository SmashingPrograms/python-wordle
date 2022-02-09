import random




def green_background(str):
  return "\33[7;49;32m " + str + " \33[0;49;37m"

def gray_background(str):
  return "\33[7;49;90m " + str + " \33[0;49;37m"

def yellow_background(str):
  return "\33[7;49;93m " + str + " \33[0;49;37m"

blank_space = " _ "
blank_space_row = f"{blank_space * 5}\n"



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

tries = 6

guesses = []

while 1:
  print("Guesses: ", guesses)
  guesses_display = "\n".join(guesses) + "\n" + (blank_space_row * tries)
  print(guesses_display)
  guess = input("Try to guess the 5-letter word: ").upper()

  colored_guess = []

  if guess == "":
    print("Please type something!")
    continue
  # elif guess not in word_list and len(guess) == 5:
  #   print("That's not a known word!")
  #   continue
  elif len(guess) != 5:
    print("Please guess a 5-letter word only!")
    continue
  else:
    tries -= 1
    guess_iterated = []
    for letter in guess:
      if secret_word[len(guess_iterated)] == letter:
        print(letter, "IS in", secret_word, "AND IT IS GREEN")
        colored_guess.append(green_background(letter))
        #Checks for earlier instances. Test this by using DRUPA with a guess of KARMA, or BABBA with ABAAA, ABBAA, BBBAA, etc.
        print(guess_iterated)
        if guess_iterated.count(letter)+1 > secret_word.count(letter):
          print("Yup it's bigger!!!!!")
          for i in range(1, len(colored_guess)):
            if guess_iterated.count(letter)+1 == secret_word.count(letter):
              break
            i = -i
            if "93" in colored_guess[i] and colored_guess[i][11] == letter:
              colored_guess[i] = gray_background(letter)
      elif letter in secret_word and guess_iterated.count(letter) < secret_word.count(letter):
        colored_guess.append(yellow_background(letter))
      else:
        colored_guess.append(gray_background(letter))
        print(letter, "is NOT in", secret_word)
      guess_iterated.append(letter)

  colored_guess = "".join(colored_guess)
  guesses.append(colored_guess)

  if guess == secret_word:
    print("YOU WIN!")
    winning_guesses_display = "\n".join(guesses)
    print(guesses_display)
    break


# list_of_words = []
# for word in old_word_list:
#   print(word)
#   print(len(word))
#   if len(word) == 5:
#     list_of_words.append(word)

# print(list_of_words)
# print(len(list_of_words))