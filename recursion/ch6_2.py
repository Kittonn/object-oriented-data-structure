def check_parindrome(inputs, start, end):
  print(start, inputs[start], end, inputs[end])
  if start == end:
    return True
  if inputs[start] != inputs[end]:
    return False
  if start < end - 1:
    return check_parindrome(inputs, start + 1, end - 1)
  return True


inputs = input("Enter Input : ")
start, end = 0, len(inputs) - 1
check = check_parindrome(inputs, start, end)
if check == True:
  print(f"'{inputs}' is palindrome")
else:
  print(f"'{inputs}' is not palindrome")
