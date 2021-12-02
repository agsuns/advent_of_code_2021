lines = []
counter = 0

#reading file
with open('./input.txt', 'r') as f:
  lines = f.readlines()

# string to int
for i in range(len(lines)):
  lines[i] = int(lines[i])

for i in range(len(lines)):
  if (i > 0):
    if (lines[i] > lines[i - 1]):
       counter += 1


print(counter)