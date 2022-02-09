def green_background(str):
  return "\33[7;49;32m" + str + "\33[0;49;37m"

def gray_background(str):
  return "\33[7;49;90m" + str + "\33[0;49;37m"

def yellow_background(str):
  return "\33[7;49;93m" + str + "\33[0;49;37m"

print(yellow_background("Hey!"))
print(gray_background("Hey!"))
print(green_background("Hey!"))

print("Hello")