import re
lines = []
horizontal = 0
depth = 0

#getting the input as an array
with open('./input.txt', 'r') as f:
  lines = f.readlines()

#function that receives a line, check the command and ultimately modifies the horizontal or the depth values
for line in lines:
  match = re.search(r"(forward|up|down) (\d{1})", line)
  
  if (match.group(1) == 'forward'):
    horizontal += int(match.group(2))
  elif (match.group(1) == 'up'):
    depth -= int(match.group(2))
  elif (match.group(1) == 'down'):
    depth += int(match.group(2))


print(depth * horizontal)


