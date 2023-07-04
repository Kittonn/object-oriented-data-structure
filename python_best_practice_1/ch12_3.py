print(" *** String count ***")
sentence = input("Enter message : ")

upper = []
lower = []

for i in sentence:
  if (i.isupper()):
    upper.append(i)
  elif (i.islower()):
    lower.append(i)

print(f'No. of Upper case characters : {len(upper)}')
print('Unique Upper case characters : ', end='')

sort_upper = sorted(set(upper))

for i in sort_upper:
  print(f'{i}  ', end='')

print()

print(f'No. of Lower case Characters : {len(lower)}')
print('Unique Lower case characters : ', end='')

sort_lower = sorted(set(lower))
for i in sort_lower:
  print(f'{i}  ', end='')
