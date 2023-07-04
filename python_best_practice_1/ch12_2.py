print(' *** Rank score ***')

scores = [i for i in input('Enter ID and Score end with ID : ').split()]

student_id = scores[-1]
scores = scores[:-1]

print([i for i in scores])
print(int(student_id))

scores_dict = {scores[i]: float(scores[i+1])
               for i in range(0, len(scores) - 1, 2)}
print(scores_dict)

num = 1
for i in scores_dict.keys():
  if (student_id == i):
    break
  num += 1
print(num)
