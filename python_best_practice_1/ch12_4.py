print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split()

rotate_str1, rotate_str2 = str1, str2

count = 1

finish = is_printed = False

while (True):
  rotate_str1 = rotate_str1[-1] + rotate_str1[:-1]
  rotate_str2 = rotate_str2[1:] + rotate_str2[0]
  if rotate_str1 == str1 and rotate_str2 == str2:
    finish = True

  if count <= 5 or finish:
    print(f'{count} {rotate_str1} {rotate_str2}')
  elif not is_printed:
    print(" . . . . . ")
    is_printed = True

  if finish:
    print(f"Total of  {count} rounds.")
    break
  count += 1
