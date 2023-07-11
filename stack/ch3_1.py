def is_valid_parentheses(parens):
  opening = ['(', '[']
  closing = [')', ']']

  stack = []

  for i in parens:
    if i in opening:
      stack.append(i)
    elif i in closing:
      if stack and stack[-1] == opening[closing.index(i)]:
        stack.pop()
      else: 
        stack.append(i)
  
  return len(stack)

parens = input('Enter Input : ')
valid = is_valid_parentheses(parens)

if valid == 0:
  print(f'{valid}\nPerfect ! ! !')
else:
  print(valid)
