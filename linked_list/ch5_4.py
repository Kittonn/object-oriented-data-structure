class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.down = None


class Snode:
  def __init__(self, data):
    self.data = data
    self.down = None


class link:
  def __init__(self):
    self.head = None

  def next_node(self, data):
    if self.search(data.data):
      return
    if self.head is None:
      self.head = data
    else:
      cur = self.head
      while cur.next is not None:
        cur = cur.next
      cur.next = data

  def search(self, data):
    cur = self.head
    while cur is not None and cur.data != data:
      cur = cur.next
    return cur

  def next_secondary_node(self, n, data):
    cur = self.search(n)
    if cur.down is None:
      cur.down = data
    else:
      cur_down = cur.down
      while cur_down.down is not None:
        cur_down = cur_down.down
      cur_down.down = data


  def show_all(self):
    cur = self.head
    while cur is not None:
      print(f'{cur.data} : ',end="")
      cur_down = cur.down
      while cur_down is not None:
        print(f'{cur_down.data},', end='')
        cur_down = cur_down.down
      cur = cur.next
      print()
      

inp = input("input : ").split(",")
l = link()
for i in inp:
  u = i.split(" ")
  if u[0] == "ADN":
    l.next_node(node(u[1]))
  elif u[0] == "ADSN":
    h = u[1].split("-")
    l.next_secondary_node(h[0], Snode(h[1]))
l.show_all()
