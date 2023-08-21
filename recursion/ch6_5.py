def generate_permutations(strings, k, start=0, result=None):
  if result is None:
    result = []

  if start == len(strings) - 1:
    result.append("".join(strings[:k]))

  for i in range(start, len(strings)):
    strings[start], strings[i] = strings[i], strings[start]
    if start == k - 1:
      result.append("".join(strings[:k]))
    else:
      generate_permutations(strings, k, start + 1, result)
    strings[start], strings[i] = strings[i], strings[start]

  return result


def permute_string(strings, k):
  if k < 0:
    print("Invalid value of k. k must be a non-negative integer.")
  elif k > len(strings):
    print("Invalid value of k. k must be less than or equal to the length of the string.")
  elif k == 0:
    print([''])
  else:
    result = generate_permutations(list(strings), k)
    print(sorted(set(result)))


if __name__ == "__main__":
  strings, k = input("Enter a string and k: ").split("/")
  permute_string(strings, int(k))
