def is_palindrome(start, end):
  if start >= end:
    return True
  if inputs[start] != inputs[end]:
    return False
  return is_palindrome(start + 1, end - 1)


if __name__ == "__main__":
  inputs = input("Enter Input: ")
  if is_palindrome(0, len(inputs) - 1):
    print(f"'{inputs}' is a palindrome")
  else:
    print(f"'{inputs}' is not a palindrome")
