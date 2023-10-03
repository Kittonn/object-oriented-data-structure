def check_isomorphic(word1, word2):
  max_count = 256

  if len(word1) != len(word2):
    return False
  
  marked = [False] * max_count

  map = [-1] * max_count

  for i in range(len(word1)):
    if map[ord(word1[i])] == -1:
      if marked[ord(word2[i])] == True:
        return False
      marked[ord(word2[i])] = True
      map[ord(word1[i])] = word2[i]
    elif map[ord(word1[i])] != word2[i]:
      return False

  return True

if __name__ == '__main__':
  word1, word2 = input('Enter str1,str2: ').split(',')
  
  check = check_isomorphic(word1, word2)

  if check:
    print(f'{word1} and {word2} are Isomorphic')
  else:
    print(f'{word1} and {word2} are not Isomorphic')