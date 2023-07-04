class TorKham:

  def __init__(self):

    self.words = []

  def restart(self):
    self.words= []
    return "game restarted"
  
  def check_word_match(self, word):
    if not self.words:
      return True
    if self.words[-1][-2:].lower() == word[:2].lower():
      return True
    return False

  def play(self, word):
    word_match = self.check_word_match(word)
    if word not in self.words and word_match:
      self.words.append(word)
      return f"'{word}' -> {self.words}"

    return f"'{word}' -> game over"


torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

S = [i.split() for i in S]

for i in S:
  
    if i[0] == "P":
  
      print(torkham.play(i[1]))
  
    elif i[0] == "R":
  
      print(torkham.restart())
      
    elif i[0] == "X":
      break
  
    else:
  
      print(f"'{i[0]} {i[1]}' is Invalid Input !!!")
  
      break