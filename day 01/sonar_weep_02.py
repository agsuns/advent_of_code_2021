lines = []
helper = []
counter = 0

#reading file
with open('./input.txt', 'r') as f:
  lines = f.readlines()

# string to int
for i in range(len(lines)):
  lines[i] = int(lines[i])

#pushes the sums in a helper array
for i in range(len(lines)):
  if (i + 3 - 1 >= len(lines)):
    break

  temp = 0
  for j in range(3):
    temp += lines[i + j]

  helper.append(temp)

#compares the values in the helper array
for i in range(len(helper)):
  if (i > 0):
    if (helper[i] > helper[i - 1]):
      counter += 1

print(counter)

