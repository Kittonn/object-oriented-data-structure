print('*** Reading E-Book ***')

text, highlight = input('Text , Highlight : ').split(',')

for i in text:
  if i == highlight:
    print(f'[{i}]', end='')
  else:
    print(i, end='')
