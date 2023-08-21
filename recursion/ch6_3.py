def jump(start, end, count):
  count += 1
  if start % 14 == 0 and start != 0:
    return
  if start == end:
    global max_way
    max_way += 1
    global distance
    distance.append(count)
    return
  if start > end:
    return
  else:
    jump(start + 1, end, count)
    jump(start + 5, end, count)
    jump(start + 7, end, count)


if __name__ == "__main__":
  n = int(input("Input number : "))
  max_way = 0
  distance = []
  c = 0
  jump(0, n, c)
  if (max_way == 0):
    print("Mission Failed")
  else:
    print(f"Minimum Distance is {min(distance) - 1}")
    print(f"Maximum Way is {max_way}")
