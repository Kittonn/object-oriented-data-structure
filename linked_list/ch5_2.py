class DoublyLinkedList:
  class Node:
    def __init__(self, element) -> None:
      self.element = element
      self.prev = None
      self.next = None

  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0

  def size(self) -> int:
    return self.size

  def isEmpty(self) -> bool:
    return self.size == 0

  def append(self, element):
    new_node = self.Node(element)
    if self.isEmpty():
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.size += 1

  def remove_tail(self):
    tail = self.tail
    before_tail = self.tail.prev
    if before_tail is not None:
      self.tail = before_tail
      self.tail.next = None
    else:
      self.head = self.tail = None
    self.size -= 1
    return tail

  def __str__(self) -> str:
    cur = self.head
    s = ""
    while cur is not None:
      s += cur.element
      cur = cur.next
    return s


doubly = DoublyLinkedList()
inputs = input("Enter Input : ").split(",")
history = []
future = []
for i in inputs:
  if len(i) == 1:
    if i == "B":
      theFuture.append(doubly.remove_tail().element)
      if not doubly.isEmpty():
        history.append(doubly.tail.element)
    elif i == "F":
      elem = theFuture.pop()
      doubly.append(elem)
      history.append(elem)
    continue

  elem = i.split(" ")[1]
  doubly.append(elem)
  history.append(elem)
  theFuture = []

backpath = []

history_output = " -> ".join(history)
print(f"History : {history_output}")

while not doubly.isEmpty():
  backpath.append(doubly.remove_tail().element)

backpath_output = " -> ".join(backpath)
print(f"BackPath : {backpath_output}")
