import re
lines = []
horizontal = 0
depth = 0
aim = 0

#getting the input as an array
with open('./input.txt', 'r') as f:
  lines = f.readlines()

for line in lines:
  match = re.search(r"(forward|up|down) (\d{1})", line)
  
  if (match.group(1) == 'forward'):
    horizontal += int(match.group(2))
    depth += int(match.group(2)) * aim
  elif (match.group(1) == 'up'):    
    aim -= int(match.group(2))
  elif (match.group(1) == 'down'):    
    aim += int(match.group(2))


print(depth * horizontal)