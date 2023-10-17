def check_isomorphic(word1, word2):
  max_char = 256
  if len(word1) != len(word2):
    return False
  
  map = [-1] * max_char
  marked = [False] * max_char

  for i in range(len(word1)):
    if map[ord(word1[i])] == -1:
      if marked[ord(word2[i])] == True:
        return False
      marked[ord(word2[i])] = True
      map[ord(word1[i])] = word2[i]
    elif map[ord(word1[i])] != word2[i]:
      return False
    
  return True